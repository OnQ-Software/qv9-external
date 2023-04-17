import json
import sys
import os

filename = os.getenv("QLIMS_BRIDGE_FILENAME")

class BridgeOutput:
    def __init__(self):
        self.operations = []
        self.manual_review = False
        self.output_message = ""

    def print(self):
        toReturn = json.dump(self.__dict__, sys.stdout)

    def operations_contains(self, filter):
        for x in self.operations:
            if filter(x):
                return True
        return False

    @staticmethod
    def bridge_operation(typ, action, match={}, setter={}):
        return {
            "type": typ,
            "action": action,
            "match": match,
            "set": setter,
		}

    def add_output_message(self, message, end="\n"):
        """
        Adds message to output. By default will append a newline at the end.
        Assign a value to the optional end argument to change how the line will
        end.
        """
        self.output_message += message + end

    def update_operation_set_value(self, match, newToSet, partialMatch=False):
        """
        Searches for an existing operation by its match values, and replaces
        its set values with the new, provided ones. Set partialMatch to True to
        replace "set" on any operation that only partially matches the given
        match dictionary.
        """
        for op in self.operations:
            if partialMatch:
                matched = all(key in op["match"] and op["match"][key] == match[key] for key in match)
            else:
                matched = op["match"] == match

            if matched:
                op["set"] = newToSet

    ### start operation methods

	## ActionAnalysts
    def create_action_analysts_operation(self, toSet):
        return self.bridge_operation("ACTION_ANALYSTS", "create", {}, toSet)

    def add_create_action_analysts_operation(self, toSet):
        self.operations.append(self.create_action_analysts_operation(toSet))

    def update_action_analysts_operation(self, match, toSet):
        return self.bridge_operation("ACTION_ANALYSTS", "update", match, toSet)

    def add_update_action_analysts_operation(self, match, toSet):
        self.operations.append(self.update_action_analysts_operation(match, toSet))

    def upsert_action_analysts_operation(self, match, toSet):
        return self.bridge_operation("ACTION_ANALYSTS", "upsert", match, toSet)

    def add_upsert_action_analysts_operation(self, match, toSet):
        self.operations.append(self.upsert_action_analysts_operation(match, toSet))

    ## Address
    def create_address_operation(self, toSet):
        return self.bridge_operation("ADDRESS", "create", {}, toSet)

    def add_create_address_operation(self, toSet):
        self.operations.append(self.create_address_operation(toSet))

    def update_address_operation(self, match, toSet):
        return self.bridge_operation("ADDRESS", "update", match, toSet)

    def add_update_address_operation(self, match, toSet):
        self.operations.append(self.update_address_operation(match, toSet))

    def upsert_address_operation(self, match, toSet):
        return self.bridge_operation("ADDRESS", "upsert", match, toSet)

    def add_upsert_address_operation(self, match, toSet):
        self.operations.append(self.upsert_address_operation(match, toSet))

    ## Attachment
    def create_attachment_operation(self, toSet):
        return self.bridge_operation("ATTACHMENT", "create", {}, toSet)

    def add_create_attachment_operation(self, toSet):
        self.operations.append(self.create_attachment_operation(toSet))

    def update_attachment_operation(self, match, toSet):
        return self.bridge_operation("ATTACHMENT", "update", match, toSet)

    def add_update_attachment_operation(self, match, toSet):
        self.operations.append(self.update_attachment_operation(match, toSet))

    def upsert_attachment_operation(self, match, toSet):
        return self.bridge_operation("ATTACHMENT", "upsert", match, toSet)

    def add_upsert_attachment_operation(self, match, toSet):
        self.operations.append(self.upsert_attachment_operation(match, toSet))

    ## Barcode
    def create_barcode_operation(self, toSet):
        return self.bridge_operation("BARCODE", "create", {}, toSet)

    def add_create_barcode_operation(self, toSet):
        self.operations.append(self.create_barcode_operation(toSet))

    def update_barcode_operation(self, match, toSet):
        return self.bridge_operation("BARCODE", "update", match, toSet)

    def add_update_barcode_operation(self, match, toSet):
        self.operations.append(self.update_barcode_operation(match, toSet))

    def upsert_barcode_operation(self, match, toSet):
        return self.bridge_operation("BARCODE", "upsert", match, toSet)

    def add_upsert_barcode_operation(self, match, toSet):
        self.operations.append(self.upsert_barcode_operation(match, toSet))

    ## BatchDetail
    def create_batch_detail_operation(self, toSet):
        return self.bridge_operation("BATCH_DETAIL", "create", {}, toSet)

    def add_create_batch_detail_operation(self, toSet):
        self.operations.append(self.create_batch_detail_operation(toSet))

    def update_batch_detail_operation(self, match, toSet):
        return self.bridge_operation("BATCH_DETAIL", "update", match, toSet)

    def add_update_batch_detail_operation(self, match, toSet):
        self.operations.append(self.update_batch_detail_operation(match, toSet))

    def upsert_batch_detail_operation(self, match, toSet):
        return self.bridge_operation("BATCH_DETAIL", "upsert", match, toSet)

    def add_upsert_batch_detail_operation(self, match, toSet):
        self.operations.append(self.upsert_batch_detail_operation(match, toSet))

    ## BatchRun
    def create_batch_run_operation(self, toSet):
        return self.bridge_operation("BATCH_RUN", "create", {}, toSet)

    def add_create_batch_run_operation(self, toSet):
        self.operations.append(self.create_batch_run_operation(toSet))

    def update_batch_run_operation(self, match, toSet):
        return self.bridge_operation("BATCH_RUN", "update", match, toSet)

    def add_update_batch_run_operation(self, match, toSet):
        self.operations.append(self.update_batch_run_operation(match, toSet))

    def upsert_batch_run_operation(self, match, toSet):
        return self.bridge_operation("BATCH_RUN", "upsert", match, toSet)

    def add_upsert_batch_run_operation(self, match, toSet):
        self.operations.append(self.upsert_batch_run_operation(match, toSet))

    ## BatchSequence
    def create_batch_sequence_operation(self, toSet):
        return self.bridge_operation("BATCH_SEQUENCE", "create", {}, toSet)

    def add_create_batch_sequence_operation(self, toSet):
        self.operations.append(self.create_batch_sequence_operation(toSet))

    def update_batch_sequence_operation(self, match, toSet):
        return self.bridge_operation("BATCH_SEQUENCE", "update", match, toSet)

    def add_update_batch_sequence_operation(self, match, toSet):
        self.operations.append(self.update_batch_sequence_operation(match, toSet))

    def upsert_batch_sequence_operation(self, match, toSet):
        return self.bridge_operation("BATCH_SEQUENCE", "upsert", match, toSet)

    def add_upsert_batch_sequence_operation(self, match, toSet):
        self.operations.append(self.upsert_batch_sequence_operation(match, toSet))

    ## BridgeProcess
    def create_bridge_process_operation(self, toSet):
        return self.bridge_operation("BRIDGE_PROCESS", "create", {}, toSet)

    def add_create_bridge_process_operation(self, toSet):
        self.operations.append(self.create_bridge_process_operation(toSet))

    def update_bridge_process_operation(self, match, toSet):
        return self.bridge_operation("BRIDGE_PROCESS", "update", match, toSet)

    def add_update_bridge_process_operation(self, match, toSet):
        self.operations.append(self.update_bridge_process_operation(match, toSet))

    def upsert_bridge_process_operation(self, match, toSet):
        return self.bridge_operation("BRIDGE_PROCESS", "upsert", match, toSet)

    def add_upsert_bridge_process_operation(self, match, toSet):
        self.operations.append(self.upsert_bridge_process_operation(match, toSet))

    ## BulkJobs
    def create_bulk_jobs_operation(self, toSet):
        return self.bridge_operation("BULK_JOBS", "create", {}, toSet)

    def add_create_bulk_jobs_operation(self, toSet):
        self.operations.append(self.create_bulk_jobs_operation(toSet))

    def update_bulk_jobs_operation(self, match, toSet):
        return self.bridge_operation("BULK_JOBS", "update", match, toSet)

    def add_update_bulk_jobs_operation(self, match, toSet):
        self.operations.append(self.update_bulk_jobs_operation(match, toSet))

    def upsert_bulk_jobs_operation(self, match, toSet):
        return self.bridge_operation("BULK_JOBS", "upsert", match, toSet)

    def add_upsert_bulk_jobs_operation(self, match, toSet):
        self.operations.append(self.upsert_bulk_jobs_operation(match, toSet))

    ## ChainOfCustody
    def create_chain_of_custody_operation(self, toSet):
        return self.bridge_operation("CHAIN_OF_CUSTODY", "create", {}, toSet)

    def add_create_chain_of_custody_operation(self, toSet):
        self.operations.append(self.create_chain_of_custody_operation(toSet))

    def update_chain_of_custody_operation(self, match, toSet):
        return self.bridge_operation("CHAIN_OF_CUSTODY", "update", match, toSet)

    def add_update_chain_of_custody_operation(self, match, toSet):
        self.operations.append(self.update_chain_of_custody_operation(match, toSet))

    def upsert_chain_of_custody_operation(self, match, toSet):
        return self.bridge_operation("CHAIN_OF_CUSTODY", "upsert", match, toSet)

    def add_upsert_chain_of_custody_operation(self, match, toSet):
        self.operations.append(self.upsert_chain_of_custody_operation(match, toSet))

    ## CocDetail
    def create_coc_detail_operation(self, toSet):
        return self.bridge_operation("COC_DETAIL", "create", {}, toSet)

    def add_create_coc_detail_operation(self, toSet):
        self.operations.append(self.create_coc_detail_operation(toSet))

    def update_coc_detail_operation(self, match, toSet):
        return self.bridge_operation("COC_DETAIL", "update", match, toSet)

    def add_update_coc_detail_operation(self, match, toSet):
        self.operations.append(self.update_coc_detail_operation(match, toSet))

    def upsert_coc_detail_operation(self, match, toSet):
        return self.bridge_operation("COC_DETAIL", "upsert", match, toSet)

    def add_upsert_coc_detail_operation(self, match, toSet):
        self.operations.append(self.upsert_coc_detail_operation(match, toSet))

    ## Contact
    def create_contact_operation(self, toSet):
        return self.bridge_operation("CONTACT", "create", {}, toSet)

    def add_create_contact_operation(self, toSet):
        self.operations.append(self.create_contact_operation(toSet))

    def update_contact_operation(self, match, toSet):
        return self.bridge_operation("CONTACT", "update", match, toSet)

    def add_update_contact_operation(self, match, toSet):
        self.operations.append(self.update_contact_operation(match, toSet))

    def upsert_contact_operation(self, match, toSet):
        return self.bridge_operation("CONTACT", "upsert", match, toSet)

    def add_upsert_contact_operation(self, match, toSet):
        self.operations.append(self.upsert_contact_operation(match, toSet))

    ## Dashboard
    def create_dashboard_operation(self, toSet):
        return self.bridge_operation("DASHBOARD", "create", {}, toSet)

    def add_create_dashboard_operation(self, toSet):
        self.operations.append(self.create_dashboard_operation(toSet))

    def update_dashboard_operation(self, match, toSet):
        return self.bridge_operation("DASHBOARD", "update", match, toSet)

    def add_update_dashboard_operation(self, match, toSet):
        self.operations.append(self.update_dashboard_operation(match, toSet))

    def upsert_dashboard_operation(self, match, toSet):
        return self.bridge_operation("DASHBOARD", "upsert", match, toSet)

    def add_upsert_dashboard_operation(self, match, toSet):
        self.operations.append(self.upsert_dashboard_operation(match, toSet))

    ## DeletedSamples
    def create_deleted_samples_operation(self, toSet):
        return self.bridge_operation("DELETED_SAMPLES", "create", {}, toSet)

    def add_create_deleted_samples_operation(self, toSet):
        self.operations.append(self.create_deleted_samples_operation(toSet))

    def update_deleted_samples_operation(self, match, toSet):
        return self.bridge_operation("DELETED_SAMPLES", "update", match, toSet)

    def add_update_deleted_samples_operation(self, match, toSet):
        self.operations.append(self.update_deleted_samples_operation(match, toSet))

    def upsert_deleted_samples_operation(self, match, toSet):
        return self.bridge_operation("DELETED_SAMPLES", "upsert", match, toSet)

    def add_upsert_deleted_samples_operation(self, match, toSet):
        self.operations.append(self.upsert_deleted_samples_operation(match, toSet))

    ## Email
    def create_email_operation(self, toSet):
        return self.bridge_operation("EMAIL", "create", {}, toSet)

    def add_create_email_operation(self, toSet):
        self.operations.append(self.create_email_operation(toSet))

    def update_email_operation(self, match, toSet):
        return self.bridge_operation("EMAIL", "update", match, toSet)

    def add_update_email_operation(self, match, toSet):
        self.operations.append(self.update_email_operation(match, toSet))

    def upsert_email_operation(self, match, toSet):
        return self.bridge_operation("EMAIL", "upsert", match, toSet)

    def add_upsert_email_operation(self, match, toSet):
        self.operations.append(self.upsert_email_operation(match, toSet))

    ## InstEvent
    def create_inst_event_operation(self, toSet):
        return self.bridge_operation("INST_EVENT", "create", {}, toSet)

    def add_create_inst_event_operation(self, toSet):
        self.operations.append(self.create_inst_event_operation(toSet))

    def update_inst_event_operation(self, match, toSet):
        return self.bridge_operation("INST_EVENT", "update", match, toSet)

    def add_update_inst_event_operation(self, match, toSet):
        self.operations.append(self.update_inst_event_operation(match, toSet))

    def upsert_inst_event_operation(self, match, toSet):
        return self.bridge_operation("INST_EVENT", "upsert", match, toSet)

    def add_upsert_inst_event_operation(self, match, toSet):
        self.operations.append(self.upsert_inst_event_operation(match, toSet))

    ## Instrument
    def create_instrument_operation(self, toSet):
        return self.bridge_operation("INSTRUMENT", "create", {}, toSet)

    def add_create_instrument_operation(self, toSet):
        self.operations.append(self.create_instrument_operation(toSet))

    def update_instrument_operation(self, match, toSet):
        return self.bridge_operation("INSTRUMENT", "update", match, toSet)

    def add_update_instrument_operation(self, match, toSet):
        self.operations.append(self.update_instrument_operation(match, toSet))

    def upsert_instrument_operation(self, match, toSet):
        return self.bridge_operation("INSTRUMENT", "upsert", match, toSet)

    def add_upsert_instrument_operation(self, match, toSet):
        self.operations.append(self.upsert_instrument_operation(match, toSet))

    ## InstrumentSamples
    def create_instrument_samples_operation(self, toSet):
        return self.bridge_operation("INSTRUMENT_SAMPLES", "create", {}, toSet)

    def add_create_instrument_samples_operation(self, toSet):
        self.operations.append(self.create_instrument_samples_operation(toSet))

    def update_instrument_samples_operation(self, match, toSet):
        return self.bridge_operation("INSTRUMENT_SAMPLES", "update", match, toSet)

    def add_update_instrument_samples_operation(self, match, toSet):
        self.operations.append(self.update_instrument_samples_operation(match, toSet))

    def upsert_instrument_samples_operation(self, match, toSet):
        return self.bridge_operation("INSTRUMENT_SAMPLES", "upsert", match, toSet)

    def add_upsert_instrument_samples_operation(self, match, toSet):
        self.operations.append(self.upsert_instrument_samples_operation(match, toSet))

    ## InstStats
    def create_inst_stats_operation(self, toSet):
        return self.bridge_operation("INST_STATS", "create", {}, toSet)

    def add_create_inst_stats_operation(self, toSet):
        self.operations.append(self.create_inst_stats_operation(toSet))

    def update_inst_stats_operation(self, match, toSet):
        return self.bridge_operation("INST_STATS", "update", match, toSet)

    def add_update_inst_stats_operation(self, match, toSet):
        self.operations.append(self.update_inst_stats_operation(match, toSet))

    def upsert_inst_stats_operation(self, match, toSet):
        return self.bridge_operation("INST_STATS", "upsert", match, toSet)

    def add_upsert_inst_stats_operation(self, match, toSet):
        self.operations.append(self.upsert_inst_stats_operation(match, toSet))

    ## Lfnr
    def create_lfnr_operation(self, toSet):
        return self.bridge_operation("LFNR", "create", {}, toSet)

    def add_create_lfnr_operation(self, toSet):
        self.operations.append(self.create_lfnr_operation(toSet))

    def update_lfnr_operation(self, match, toSet):
        return self.bridge_operation("LFNR", "update", match, toSet)

    def add_update_lfnr_operation(self, match, toSet):
        self.operations.append(self.update_lfnr_operation(match, toSet))

    def upsert_lfnr_operation(self, match, toSet):
        return self.bridge_operation("LFNR", "upsert", match, toSet)

    def add_upsert_lfnr_operation(self, match, toSet):
        self.operations.append(self.upsert_lfnr_operation(match, toSet))

    ## LimsEvent
    def create_lims_event_operation(self, toSet):
        return self.bridge_operation("LIMS_EVENT", "create", {}, toSet)

    def add_create_lims_event_operation(self, toSet):
        self.operations.append(self.create_lims_event_operation(toSet))

    def update_lims_event_operation(self, match, toSet):
        return self.bridge_operation("LIMS_EVENT", "update", match, toSet)

    def add_update_lims_event_operation(self, match, toSet):
        self.operations.append(self.update_lims_event_operation(match, toSet))

    def upsert_lims_event_operation(self, match, toSet):
        return self.bridge_operation("LIMS_EVENT", "upsert", match, toSet)

    def add_upsert_lims_event_operation(self, match, toSet):
        self.operations.append(self.upsert_lims_event_operation(match, toSet))

    ## LimsQuery
    def create_lims_query_operation(self, toSet):
        return self.bridge_operation("LIMS_QUERY", "create", {}, toSet)

    def add_create_lims_query_operation(self, toSet):
        self.operations.append(self.create_lims_query_operation(toSet))

    def update_lims_query_operation(self, match, toSet):
        return self.bridge_operation("LIMS_QUERY", "update", match, toSet)

    def add_update_lims_query_operation(self, match, toSet):
        self.operations.append(self.update_lims_query_operation(match, toSet))

    def upsert_lims_query_operation(self, match, toSet):
        return self.bridge_operation("LIMS_QUERY", "upsert", match, toSet)

    def add_upsert_lims_query_operation(self, match, toSet):
        self.operations.append(self.upsert_lims_query_operation(match, toSet))

    ## Lookup
    def create_lookup_operation(self, toSet):
        return self.bridge_operation("LOOKUP", "create", {}, toSet)

    def add_create_lookup_operation(self, toSet):
        self.operations.append(self.create_lookup_operation(toSet))

    def update_lookup_operation(self, match, toSet):
        return self.bridge_operation("LOOKUP", "update", match, toSet)

    def add_update_lookup_operation(self, match, toSet):
        self.operations.append(self.update_lookup_operation(match, toSet))

    def upsert_lookup_operation(self, match, toSet):
        return self.bridge_operation("LOOKUP", "upsert", match, toSet)

    def add_upsert_lookup_operation(self, match, toSet):
        self.operations.append(self.upsert_lookup_operation(match, toSet))

    ## Method
    def create_method_operation(self, toSet):
        return self.bridge_operation("METHOD", "create", {}, toSet)

    def add_create_method_operation(self, toSet):
        self.operations.append(self.create_method_operation(toSet))

    def update_method_operation(self, match, toSet):
        return self.bridge_operation("METHOD", "update", match, toSet)

    def add_update_method_operation(self, match, toSet):
        self.operations.append(self.update_method_operation(match, toSet))

    def upsert_method_operation(self, match, toSet):
        return self.bridge_operation("METHOD", "upsert", match, toSet)

    def add_upsert_method_operation(self, match, toSet):
        self.operations.append(self.upsert_method_operation(match, toSet))

    ## MktSynonym
    def create_mkt_synonym_operation(self, toSet):
        return self.bridge_operation("MKT_SYNONYM", "create", {}, toSet)

    def add_create_mkt_synonym_operation(self, toSet):
        self.operations.append(self.create_mkt_synonym_operation(toSet))

    def update_mkt_synonym_operation(self, match, toSet):
        return self.bridge_operation("MKT_SYNONYM", "update", match, toSet)

    def add_update_mkt_synonym_operation(self, match, toSet):
        self.operations.append(self.update_mkt_synonym_operation(match, toSet))

    def upsert_mkt_synonym_operation(self, match, toSet):
        return self.bridge_operation("MKT_SYNONYM", "upsert", match, toSet)

    def add_upsert_mkt_synonym_operation(self, match, toSet):
        self.operations.append(self.upsert_mkt_synonym_operation(match, toSet))

    ## Note
    def create_note_operation(self, toSet):
        return self.bridge_operation("NOTE", "create", {}, toSet)

    def add_create_note_operation(self, toSet):
        self.operations.append(self.create_note_operation(toSet))

    def update_note_operation(self, match, toSet):
        return self.bridge_operation("NOTE", "update", match, toSet)

    def add_update_note_operation(self, match, toSet):
        self.operations.append(self.update_note_operation(match, toSet))

    def upsert_note_operation(self, match, toSet):
        return self.bridge_operation("NOTE", "upsert", match, toSet)

    def add_upsert_note_operation(self, match, toSet):
        self.operations.append(self.upsert_note_operation(match, toSet))

    ## OosActions
    def create_oos_actions_operation(self, toSet):
        return self.bridge_operation("OOS_ACTIONS", "create", {}, toSet)

    def add_create_oos_actions_operation(self, toSet):
        self.operations.append(self.create_oos_actions_operation(toSet))

    def update_oos_actions_operation(self, match, toSet):
        return self.bridge_operation("OOS_ACTIONS", "update", match, toSet)

    def add_update_oos_actions_operation(self, match, toSet):
        self.operations.append(self.update_oos_actions_operation(match, toSet))

    def upsert_oos_actions_operation(self, match, toSet):
        return self.bridge_operation("OOS_ACTIONS", "upsert", match, toSet)

    def add_upsert_oos_actions_operation(self, match, toSet):
        self.operations.append(self.upsert_oos_actions_operation(match, toSet))

    ## OosPreventions
    def create_oos_preventions_operation(self, toSet):
        return self.bridge_operation("OOS_PREVENTIONS", "create", {}, toSet)

    def add_create_oos_preventions_operation(self, toSet):
        self.operations.append(self.create_oos_preventions_operation(toSet))

    def update_oos_preventions_operation(self, match, toSet):
        return self.bridge_operation("OOS_PREVENTIONS", "update", match, toSet)

    def add_update_oos_preventions_operation(self, match, toSet):
        self.operations.append(self.update_oos_preventions_operation(match, toSet))

    def upsert_oos_preventions_operation(self, match, toSet):
        return self.bridge_operation("OOS_PREVENTIONS", "upsert", match, toSet)

    def add_upsert_oos_preventions_operation(self, match, toSet):
        self.operations.append(self.upsert_oos_preventions_operation(match, toSet))

    ## Order
    def create_order_operation(self, toSet):
        return self.bridge_operation("ORDER", "create", {}, toSet)

    def add_create_order_operation(self, toSet):
        self.operations.append(self.create_order_operation(toSet))

    def update_order_operation(self, match, toSet):
        return self.bridge_operation("ORDER", "update", match, toSet)

    def add_update_order_operation(self, match, toSet):
        self.operations.append(self.update_order_operation(match, toSet))

    def upsert_order_operation(self, match, toSet):
        return self.bridge_operation("ORDER", "upsert", match, toSet)

    def add_upsert_order_operation(self, match, toSet):
        self.operations.append(self.upsert_order_operation(match, toSet))

    ## OutOfSpecification
    def create_out_of_specification_operation(self, toSet):
        return self.bridge_operation("OUT_OF_SPECIFICATION", "create", {}, toSet)

    def add_create_out_of_specification_operation(self, toSet):
        self.operations.append(self.create_out_of_specification_operation(toSet))

    def update_out_of_specification_operation(self, match, toSet):
        return self.bridge_operation("OUT_OF_SPECIFICATION", "update", match, toSet)

    def add_update_out_of_specification_operation(self, match, toSet):
        self.operations.append(self.update_out_of_specification_operation(match, toSet))

    def upsert_out_of_specification_operation(self, match, toSet):
        return self.bridge_operation("OUT_OF_SPECIFICATION", "upsert", match, toSet)

    def add_upsert_out_of_specification_operation(self, match, toSet):
        self.operations.append(self.upsert_out_of_specification_operation(match, toSet))

    ## Parameter
    def create_parameter_operation(self, toSet):
        return self.bridge_operation("PARAMETER", "create", {}, toSet)

    def add_create_parameter_operation(self, toSet):
        self.operations.append(self.create_parameter_operation(toSet))

    def update_parameter_operation(self, match, toSet):
        return self.bridge_operation("PARAMETER", "update", match, toSet)

    def add_update_parameter_operation(self, match, toSet):
        self.operations.append(self.update_parameter_operation(match, toSet))

    def upsert_parameter_operation(self, match, toSet):
        return self.bridge_operation("PARAMETER", "upsert", match, toSet)

    def add_upsert_parameter_operation(self, match, toSet):
        self.operations.append(self.upsert_parameter_operation(match, toSet))

    ## ParamRoundingRules
    def create_param_rounding_rules_operation(self, toSet):
        return self.bridge_operation("PARAM_ROUNDING_RULES", "create", {}, toSet)

    def add_create_param_rounding_rules_operation(self, toSet):
        self.operations.append(self.create_param_rounding_rules_operation(toSet))

    def update_param_rounding_rules_operation(self, match, toSet):
        return self.bridge_operation("PARAM_ROUNDING_RULES", "update", match, toSet)

    def add_update_param_rounding_rules_operation(self, match, toSet):
        self.operations.append(self.update_param_rounding_rules_operation(match, toSet))

    def upsert_param_rounding_rules_operation(self, match, toSet):
        return self.bridge_operation("PARAM_ROUNDING_RULES", "upsert", match, toSet)

    def add_upsert_param_rounding_rules_operation(self, match, toSet):
        self.operations.append(self.upsert_param_rounding_rules_operation(match, toSet))

    ## Ping
    def create_ping_operation(self, toSet):
        return self.bridge_operation("PING", "create", {}, toSet)

    def add_create_ping_operation(self, toSet):
        self.operations.append(self.create_ping_operation(toSet))

    def update_ping_operation(self, match, toSet):
        return self.bridge_operation("PING", "update", match, toSet)

    def add_update_ping_operation(self, match, toSet):
        self.operations.append(self.update_ping_operation(match, toSet))

    def upsert_ping_operation(self, match, toSet):
        return self.bridge_operation("PING", "upsert", match, toSet)

    def add_upsert_ping_operation(self, match, toSet):
        self.operations.append(self.upsert_ping_operation(match, toSet))

    ## PricingDetail
    def create_pricing_detail_operation(self, toSet):
        return self.bridge_operation("PRICING_DETAIL", "create", {}, toSet)

    def add_create_pricing_detail_operation(self, toSet):
        self.operations.append(self.create_pricing_detail_operation(toSet))

    def update_pricing_detail_operation(self, match, toSet):
        return self.bridge_operation("PRICING_DETAIL", "update", match, toSet)

    def add_update_pricing_detail_operation(self, match, toSet):
        self.operations.append(self.update_pricing_detail_operation(match, toSet))

    def upsert_pricing_detail_operation(self, match, toSet):
        return self.bridge_operation("PRICING_DETAIL", "upsert", match, toSet)

    def add_upsert_pricing_detail_operation(self, match, toSet):
        self.operations.append(self.upsert_pricing_detail_operation(match, toSet))

    ## Project
    def create_project_operation(self, toSet):
        return self.bridge_operation("PROJECT", "create", {}, toSet)

    def add_create_project_operation(self, toSet):
        self.operations.append(self.create_project_operation(toSet))

    def update_project_operation(self, match, toSet):
        return self.bridge_operation("PROJECT", "update", match, toSet)

    def add_update_project_operation(self, match, toSet):
        self.operations.append(self.update_project_operation(match, toSet))

    def upsert_project_operation(self, match, toSet):
        return self.bridge_operation("PROJECT", "upsert", match, toSet)

    def add_upsert_project_operation(self, match, toSet):
        self.operations.append(self.upsert_project_operation(match, toSet))

    ## ProjectBasedUser
    def create_project_based_user_operation(self, toSet):
        return self.bridge_operation("PROJECT_BASED_USER", "create", {}, toSet)

    def add_create_project_based_user_operation(self, toSet):
        self.operations.append(self.create_project_based_user_operation(toSet))

    def update_project_based_user_operation(self, match, toSet):
        return self.bridge_operation("PROJECT_BASED_USER", "update", match, toSet)

    def add_update_project_based_user_operation(self, match, toSet):
        self.operations.append(self.update_project_based_user_operation(match, toSet))

    def upsert_project_based_user_operation(self, match, toSet):
        return self.bridge_operation("PROJECT_BASED_USER", "upsert", match, toSet)

    def add_upsert_project_based_user_operation(self, match, toSet):
        self.operations.append(self.upsert_project_based_user_operation(match, toSet))

    ## ProjectTeam
    def create_project_team_operation(self, toSet):
        return self.bridge_operation("PROJECT_TEAM", "create", {}, toSet)

    def add_create_project_team_operation(self, toSet):
        self.operations.append(self.create_project_team_operation(toSet))

    def update_project_team_operation(self, match, toSet):
        return self.bridge_operation("PROJECT_TEAM", "update", match, toSet)

    def add_update_project_team_operation(self, match, toSet):
        self.operations.append(self.update_project_team_operation(match, toSet))

    def upsert_project_team_operation(self, match, toSet):
        return self.bridge_operation("PROJECT_TEAM", "upsert", match, toSet)

    def add_upsert_project_team_operation(self, match, toSet):
        self.operations.append(self.upsert_project_team_operation(match, toSet))

    ## Report
    def create_report_operation(self, toSet):
        return self.bridge_operation("REPORT", "create", {}, toSet)

    def add_create_report_operation(self, toSet):
        self.operations.append(self.create_report_operation(toSet))

    def update_report_operation(self, match, toSet):
        return self.bridge_operation("REPORT", "update", match, toSet)

    def add_update_report_operation(self, match, toSet):
        self.operations.append(self.update_report_operation(match, toSet))

    def upsert_report_operation(self, match, toSet):
        return self.bridge_operation("REPORT", "upsert", match, toSet)

    def add_upsert_report_operation(self, match, toSet):
        self.operations.append(self.upsert_report_operation(match, toSet))

    ## ReportParameter
    def create_report_parameter_operation(self, toSet):
        return self.bridge_operation("REPORT_PARAMETER", "create", {}, toSet)

    def add_create_report_parameter_operation(self, toSet):
        self.operations.append(self.create_report_parameter_operation(toSet))

    def update_report_parameter_operation(self, match, toSet):
        return self.bridge_operation("REPORT_PARAMETER", "update", match, toSet)

    def add_update_report_parameter_operation(self, match, toSet):
        self.operations.append(self.update_report_parameter_operation(match, toSet))

    def upsert_report_parameter_operation(self, match, toSet):
        return self.bridge_operation("REPORT_PARAMETER", "upsert", match, toSet)

    def add_upsert_report_parameter_operation(self, match, toSet):
        self.operations.append(self.upsert_report_parameter_operation(match, toSet))

    ## ReptDistribution
    def create_rept_distribution_operation(self, toSet):
        return self.bridge_operation("REPT_DISTRIBUTION", "create", {}, toSet)

    def add_create_rept_distribution_operation(self, toSet):
        self.operations.append(self.create_rept_distribution_operation(toSet))

    def update_rept_distribution_operation(self, match, toSet):
        return self.bridge_operation("REPT_DISTRIBUTION", "update", match, toSet)

    def add_update_rept_distribution_operation(self, match, toSet):
        self.operations.append(self.update_rept_distribution_operation(match, toSet))

    def upsert_rept_distribution_operation(self, match, toSet):
        return self.bridge_operation("REPT_DISTRIBUTION", "upsert", match, toSet)

    def add_upsert_rept_distribution_operation(self, match, toSet):
        self.operations.append(self.upsert_rept_distribution_operation(match, toSet))

    ## Results
    def create_results_operation(self, toSet):
        return self.bridge_operation("RESULTS", "create", {}, toSet)

    def add_create_results_operation(self, toSet):
        self.operations.append(self.create_results_operation(toSet))

    def update_results_operation(self, match, toSet):
        return self.bridge_operation("RESULTS", "update", match, toSet)

    def add_update_results_operation(self, match, toSet):
        self.operations.append(self.update_results_operation(match, toSet))

    def upsert_results_operation(self, match, toSet):
        return self.bridge_operation("RESULTS", "upsert", match, toSet)

    def add_upsert_results_operation(self, match, toSet):
        self.operations.append(self.upsert_results_operation(match, toSet))

    ## Sample
    def create_sample_operation(self, toSet):
        return self.bridge_operation("SAMPLE", "create", {}, toSet)

    def add_create_sample_operation(self, toSet):
        self.operations.append(self.create_sample_operation(toSet))

    def update_sample_operation(self, match, toSet):
        return self.bridge_operation("SAMPLE", "update", match, toSet)

    def add_update_sample_operation(self, match, toSet):
        self.operations.append(self.update_sample_operation(match, toSet))

    def upsert_sample_operation(self, match, toSet):
        return self.bridge_operation("SAMPLE", "upsert", match, toSet)

    def add_upsert_sample_operation(self, match, toSet):
        self.operations.append(self.upsert_sample_operation(match, toSet))

    ## SampleParameter
    def create_sample_parameter_operation(self, toSet):
        return self.bridge_operation("SAMPLEPARAM", "create", {}, toSet)

    def add_create_sample_parameter_operation(self, toSet):
        self.operations.append(self.create_sample_parameter_operation(toSet))

    def update_sample_parameter_operation(self, match, toSet):
        return self.bridge_operation("SAMPLEPARAM", "update", match, toSet)

    def add_update_sample_parameter_operation(self, match, toSet):
        self.operations.append(self.update_sample_parameter_operation(match, toSet))

    def upsert_sample_parameter_operation(self, match, toSet):
        return self.bridge_operation("SAMPLE_PARAMETER", "upsert", match, toSet)

    def add_upsert_sample_parameter_operation(self, match, toSet):
        self.operations.append(self.upsert_sample_parameter_operation(match, toSet))

    ## SampleTemplate
    def create_sample_template_operation(self, toSet):
        return self.bridge_operation("SAMPLE_TEMPLATE", "create", {}, toSet)

    def add_create_sample_template_operation(self, toSet):
        self.operations.append(self.create_sample_template_operation(toSet))

    def update_sample_template_operation(self, match, toSet):
        return self.bridge_operation("SAMPLE_TEMPLATE", "update", match, toSet)

    def add_update_sample_template_operation(self, match, toSet):
        self.operations.append(self.update_sample_template_operation(match, toSet))

    def upsert_sample_template_operation(self, match, toSet):
        return self.bridge_operation("SAMPLE_TEMPLATE", "upsert", match, toSet)

    def add_upsert_sample_template_operation(self, match, toSet):
        self.operations.append(self.upsert_sample_template_operation(match, toSet))

    ## SampleType
    def create_sample_type_operation(self, toSet):
        return self.bridge_operation("SAMPLE_TYPE", "create", {}, toSet)

    def add_create_sample_type_operation(self, toSet):
        self.operations.append(self.create_sample_type_operation(toSet))

    def update_sample_type_operation(self, match, toSet):
        return self.bridge_operation("SAMPLE_TYPE", "update", match, toSet)

    def add_update_sample_type_operation(self, match, toSet):
        self.operations.append(self.update_sample_type_operation(match, toSet))

    def upsert_sample_type_operation(self, match, toSet):
        return self.bridge_operation("SAMPLE_TYPE", "upsert", match, toSet)

    def add_upsert_sample_type_operation(self, match, toSet):
        self.operations.append(self.upsert_sample_type_operation(match, toSet))

    ## Sampmeth
    def create_sampmeth_operation(self, toSet):
        return self.bridge_operation("SAMPMETH", "create", {}, toSet)

    def add_create_sampmeth_operation(self, toSet):
        self.operations.append(self.create_sampmeth_operation(toSet))

    def update_sampmeth_operation(self, match, toSet):
        return self.bridge_operation("SAMPMETH", "update", match, toSet)

    def add_update_sampmeth_operation(self, match, toSet):
        self.operations.append(self.update_sampmeth_operation(match, toSet))

    def upsert_sampmeth_operation(self, match, toSet):
        return self.bridge_operation("SAMPMETH", "upsert", match, toSet)

    def add_upsert_sampmeth_operation(self, match, toSet):
        self.operations.append(self.upsert_sampmeth_operation(match, toSet))

    ## Samtypmeth
    def create_samtypmeth_operation(self, toSet):
        return self.bridge_operation("SAMTYPMETH", "create", {}, toSet)

    def add_create_samtypmeth_operation(self, toSet):
        self.operations.append(self.create_samtypmeth_operation(toSet))

    def update_samtypmeth_operation(self, match, toSet):
        return self.bridge_operation("SAMTYPMETH", "update", match, toSet)

    def add_update_samtypmeth_operation(self, match, toSet):
        self.operations.append(self.update_samtypmeth_operation(match, toSet))

    def upsert_samtypmeth_operation(self, match, toSet):
        return self.bridge_operation("SAMTYPMETH", "upsert", match, toSet)

    def add_upsert_samtypmeth_operation(self, match, toSet):
        self.operations.append(self.upsert_samtypmeth_operation(match, toSet))

    ## Samtypparam
    def create_samtypparam_operation(self, toSet):
        return self.bridge_operation("SAMTYPPARAM", "create", {}, toSet)

    def add_create_samtypparam_operation(self, toSet):
        self.operations.append(self.create_samtypparam_operation(toSet))

    def update_samtypparam_operation(self, match, toSet):
        return self.bridge_operation("SAMTYPPARAM", "update", match, toSet)

    def add_update_samtypparam_operation(self, match, toSet):
        self.operations.append(self.update_samtypparam_operation(match, toSet))

    def upsert_samtypparam_operation(self, match, toSet):
        return self.bridge_operation("SAMTYPPARAM", "upsert", match, toSet)

    def add_upsert_samtypparam_operation(self, match, toSet):
        self.operations.append(self.upsert_samtypparam_operation(match, toSet))

    ## Staff
    def create_staff_operation(self, toSet):
        return self.bridge_operation("STAFF", "create", {}, toSet)

    def add_create_staff_operation(self, toSet):
        self.operations.append(self.create_staff_operation(toSet))

    def update_staff_operation(self, match, toSet):
        return self.bridge_operation("STAFF", "update", match, toSet)

    def add_update_staff_operation(self, match, toSet):
        self.operations.append(self.update_staff_operation(match, toSet))

    def upsert_staff_operation(self, match, toSet):
        return self.bridge_operation("STAFF", "upsert", match, toSet)

    def add_upsert_staff_operation(self, match, toSet):
        self.operations.append(self.upsert_staff_operation(match, toSet))

    ## StaffLabs
    def create_staff_labs_operation(self, toSet):
        return self.bridge_operation("STAFF_LABS", "create", {}, toSet)

    def add_create_staff_labs_operation(self, toSet):
        self.operations.append(self.create_staff_labs_operation(toSet))

    def update_staff_labs_operation(self, match, toSet):
        return self.bridge_operation("STAFF_LABS", "update", match, toSet)

    def add_update_staff_labs_operation(self, match, toSet):
        self.operations.append(self.update_staff_labs_operation(match, toSet))

    def upsert_staff_labs_operation(self, match, toSet):
        return self.bridge_operation("STAFF_LABS", "upsert", match, toSet)

    def add_upsert_staff_labs_operation(self, match, toSet):
        self.operations.append(self.upsert_staff_labs_operation(match, toSet))

    ## StParamRoundingRules
    def create_st_param_rounding_rules_operation(self, toSet):
        return self.bridge_operation("ST_PARAM_ROUNDING_RULES", "create", {}, toSet)

    def add_create_st_param_rounding_rules_operation(self, toSet):
        self.operations.append(self.create_st_param_rounding_rules_operation(toSet))

    def update_st_param_rounding_rules_operation(self, match, toSet):
        return self.bridge_operation("ST_PARAM_ROUNDING_RULES", "update", match, toSet)

    def add_update_st_param_rounding_rules_operation(self, match, toSet):
        self.operations.append(self.update_st_param_rounding_rules_operation(match, toSet))

    def upsert_st_param_rounding_rules_operation(self, match, toSet):
        return self.bridge_operation("ST_PARAM_ROUNDING_RULES", "upsert", match, toSet)

    def add_upsert_st_param_rounding_rules_operation(self, match, toSet):
        self.operations.append(self.upsert_st_param_rounding_rules_operation(match, toSet))

    ## TextBlock
    def create_text_block_operation(self, toSet):
        return self.bridge_operation("TEXT_BLOCK", "create", {}, toSet)

    def add_create_text_block_operation(self, toSet):
        self.operations.append(self.create_text_block_operation(toSet))

    def update_text_block_operation(self, match, toSet):
        return self.bridge_operation("TEXT_BLOCK", "update", match, toSet)

    def add_update_text_block_operation(self, match, toSet):
        self.operations.append(self.update_text_block_operation(match, toSet))

    def upsert_text_block_operation(self, match, toSet):
        return self.bridge_operation("TEXT_BLOCK", "upsert", match, toSet)

    def add_upsert_text_block_operation(self, match, toSet):
        self.operations.append(self.upsert_text_block_operation(match, toSet))

    ## Units
    def create_units_operation(self, toSet):
        return self.bridge_operation("UNITS", "create", {}, toSet)

    def add_create_units_operation(self, toSet):
        self.operations.append(self.create_units_operation(toSet))

    def update_units_operation(self, match, toSet):
        return self.bridge_operation("UNITS", "update", match, toSet)

    def add_update_units_operation(self, match, toSet):
        self.operations.append(self.update_units_operation(match, toSet))

    def upsert_units_operation(self, match, toSet):
        return self.bridge_operation("UNITS", "upsert", match, toSet)

    def add_upsert_units_operation(self, match, toSet):
        self.operations.append(self.upsert_units_operation(match, toSet))

    ## UserNoteReference
    def create_user_note_reference_operation(self, toSet):
        return self.bridge_operation("USER_NOTE_REFERENCE", "create", {}, toSet)

    def add_create_user_note_reference_operation(self, toSet):
        self.operations.append(self.create_user_note_reference_operation(toSet))

    def update_user_note_reference_operation(self, match, toSet):
        return self.bridge_operation("USER_NOTE_REFERENCE", "update", match, toSet)

    def add_update_user_note_reference_operation(self, match, toSet):
        self.operations.append(self.update_user_note_reference_operation(match, toSet))

    def upsert_user_note_reference_operation(self, match, toSet):
        return self.bridge_operation("USER_NOTE_REFERENCE", "upsert", match, toSet)

    def add_upsert_user_note_reference_operation(self, match, toSet):
        self.operations.append(self.upsert_user_note_reference_operation(match, toSet))

    ### end operation methods

    def output(self):
        return {
                "manual_review":self.manual_review,
                "operations":self.operations
            }

    