import os

src_directory = os.path.dirname(os.path.abspath(__file__)) 
logs_directory = os.path.join(src_directory, '..', 'logs')
audit_log_file = os.path.join(logs_directory, 'audit.log')
consent_log_file = os.path.join(logs_directory, 'consent.log')
report_file = os.path.join(logs_directory, 'compliance_report.txt')

# Additional checks
verify_withdrawal_mechanism = os.path.join(logs_directory, 'verify_withdrawal_mechanism.log')
third_party_analytics_log = os.path.join(logs_directory, 'third_party_analytics.log')


def generate_compliance_report():
    """Generate a compliance report based on the logs."""
    report = []  # List to accumulate the report content

    report.append("\nGenerating compliance report...\n")

    # Read logs
    try:
        with open(audit_log_file, 'r') as audit_file:
            audit_logs = audit_file.readlines()

        with open(consent_log_file, 'r') as consent_file:
            consent_logs = consent_file.readlines()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    # Check for relevant events in audit and consent logs
    relevant_audit_events = [log for log in audit_logs if 'sensitive' in log]
    relevant_consent_events = [log for log in consent_logs if 'privacy' in log]
    consent_withdrawals = [log for log in consent_logs if 'withdrawn' in log]

    # Add compliance report details to the report list
    report.append("\nCompliance Report")
    report.append(f"Total Audit Events: {len(audit_logs)}")
    report.append(f"Relevant Audit Events: {len(relevant_audit_events)}")
    report.append(f"Total Consent Events: {len(consent_logs)}")
    report.append(f"Relevant Consent Events: {len(relevant_consent_events)}")
    
    # Compliance Check Summary
    if relevant_audit_events and relevant_consent_events:
        report.append("\nCompliance passed: Relevant audit and consent data found.")
    else:
        report.append("\nCompliance failed: Missing relevant audit or consent data.")
        
    # Adding more detailed report output
    report.append("\nDetailed Log Entries:")
    
    if relevant_audit_events:
        report.append("\nRelevant Audit Events (sensitive data access):")
        for event in relevant_audit_events:
            report.append(f"- {event.strip()}")
    
    if relevant_consent_events:
        report.append("\nRelevant Consent Events (privacy policy consent):")
        for event in relevant_consent_events:
            report.append(f"- {event.strip()}")
            
    if consent_withdrawals:
        report.append("\nConsent Withdrawal Events:")
        for event in consent_withdrawals:
            report.append(f"- {event.strip()}")
            
    # Check for additional logs like withdrawal mechanism check and third-party analytics
    if os.path.exists(verify_withdrawal_mechanism):
        with open(verify_withdrawal_mechanism, 'r') as file:
            banner_check = file.read().strip()
        report.append(f"\nConsent Banner Check: {banner_check}")
    
    if os.path.exists(third_party_analytics_log):
        with open(third_party_analytics_log, 'r') as file:
            third_party_check = file.read().strip()
        report.append(f"\nThird-Party Analytics Check: {third_party_check}")

    # Debugging: Check the path before writing
    print("Writing report to:", report_file)
    
    # Save the report to a file
    with open(report_file, 'w') as report_file_handle:
        report_file_handle.write("\n".join(report))
        print("Report written successfully.")

if __name__ == '__main__':
    generate_compliance_report()
