from lxml import etree
import csv
import sys
from qlims.bridge import BridgeOutput
from dataclasses import dataclass
import typing
import itertools
from enum import Enum

class Action(Enum):
    CREATE = 'create'
    UPDATE = 'update'
    UPSERT = 'upsert'

@dataclass
class Event:
    data_type: str
    event_no: typing.Optional[int]
    action: Action
    match_cols: typing.MutableSequence[str]

def process_with_xslt(xslt_string, convert_from_delimited=True, delimiter=',', quotechar='"', skip_rows=0, custom_events=[]):
    xslt_transformer = etree.XSLT(etree.XML(xslt_string))
    if convert_from_delimited:
        csv_reader = csv.reader(sys.stdin, delimiter=delimiter, quotechar=quotechar)
        xml_input = delimited_text_to_xml(itertools.islice(csv_reader, skip_rows, None))
    else:
        xml_input = etree.parse(sys.stdin)
    xml_output = xslt_transformer(xml_input).getroot()
    legacy_to_BridgeOutput(xml_output, custom_events).print()

def delimited_text_to_xml(reader):
    root = etree.Element("dataRoot")
    for csv_row in reader:
        xml_row = etree.SubElement(root, "dataRow")
        for col_idx, col_text in enumerate(csv_row):
            xml_col = etree.SubElement(xml_row, f"a{col_idx}")
            xml_col.text = col_text
    return root

default_events = [
    Event('INBOX_SAMPLE', None, Action.UPDATE, ['SAMPLE_ID']),
    Event('INBOX_SAMPLE', 1, Action.CREATE, ['SAMPLE_TYPE', 'LOT', 'TEXT9']),
    #TODO Event('INBOX_SAMPLE', 2, '', ['SAMPLE_TYPE', 'LOT', 'TEXT9']),
    Event('INBOX_SAMPLE', 3, Action.CREATE, ['SAMPLE_TYPE', 'LOT', 'TEXT9']),
    #TODO Event('INBOX_SAMPLE', 4, Action., ['SAMPLE_ID']),
    #TODO Event('INBOX_SAMPLE', 5, Action., ['SAMPLE_ID']),
    #TODO Event('INBOX_SAMPLE', 6, Action., ['SAMPLE_ID']),
    #TODO Event('INBOX_SAMPLE', 7, Action., ['SAMPLE_ID']),
    #TODO Event('INBOX_SAMPLE', 8, Action., ['SAMPLE_ID']),
    #TODO Event('INBOX_SAMPLE', 9, Action., ['LOT', 'TEXT1', 'DATE1']),
    Event('INBOX_SAMPLETYPE', 1, Action.UPSERT, ['ST_ID', 'CUSTOMER_ID']),
    #TODO Event('INBOX_SAMPLETYPE', 2, Action., ['ST_ID', 'CUSTOMER_ID']),
    Event('INBOX_SAMPLETYPE', 3, Action.UPDATE, ['ST_ID', 'CUSTOMER_ID']),
    #TODO Event('INBOX_SAMPLETYPE', 4, Action., ['ST_ID', 'CUSTOMER_ID']),
    Event('INBOX_METHOD', 1, Action.UPSERT, ['NAME']),
    #TODO Event('INBOX_METHOD', 2, Action., ['NAME', 'OWNER']),
    Event('INBOX_METHOD', 3, Action.UPDATE, ['NAME', 'OWNER']),
]

def legacy_to_BridgeOutput(xml_output, custom_events):
    bridge_output = BridgeOutput()
    events = {(e.data_type, e.event_no): e for e in default_events + custom_events}
    for legacy_op in xml_output:
        to_set = {field.tag: field.text for field in legacy_op}
        event = events[(legacy_op.tag, to_set.pop('EVENT', None))] # Pop 'EVENT' from to_set, if present
        to_match = {c: to_set.pop(c) for c in event.match_cols} # Pop all match columns from to_set (presence required)
        bridge_output.operations.append(BridgeOutput.bridge_operation(
            # TODO: Match to correct view tables
            { 'INBOX_SAMPLE': 'SAMPLE', 'INBOX_SAMPLETYPE': 'SAMPLETYPE', 'INBOX_METHOD': 'METHOD', 'INBOX_PATIENT': 'PATIENT'}[event.data_type],
            event.action.value,
            match=to_match,
            set=to_set,
        ))
    return bridge_output