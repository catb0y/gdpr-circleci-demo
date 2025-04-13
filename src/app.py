import os
import time

# Paths to logs 
logs_directory = os.path.join(os.getcwd(), 'src', 'logs')
audit_log_file = os.path.join(logs_directory, 'audit.log')
consent_log_file = os.path.join(logs_directory, 'consent.log')

# Ensure the 'logs' directory exists
if not os.path.exists(logs_directory):
    os.makedirs(logs_directory)

def log_audit_event(user, event_type):
    """Log an audit event."""
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
    log_entry = f'{timestamp} - {user} performed {event_type}\n'
    
    with open(audit_log_file, 'a') as log_file:
        log_file.write(log_entry)
    print(f"Audit event logged: {log_entry.strip()}")

def log_consent_event(user, consent_type):
    """Log a consent event."""
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
    log_entry = f'{timestamp} - {user} consented to {consent_type}\n'
    
    with open(consent_log_file, 'a') as log_file:
        log_file.write(log_entry)
    print(f"Consent event logged: {log_entry.strip()}")

def generate_compliance_report():
    """Generate a compliance report based on the logs."""
    print("\nGenerating compliance report...")
    
    # Read logs
    with open(audit_log_file, 'r') as audit_file:
        audit_logs = audit_file.readlines()

    with open(consent_log_file, 'r') as consent_file:
        consent_logs = consent_file.readlines()

    # Check for relevant events
    relevant_audit_events = [log for log in audit_logs if 'sensitive' in log]
    relevant_consent_events = [log for log in consent_logs if 'privacy' in log]

    print("\nCompliance Report")
    print(f"Total Audit Events: {len(audit_logs)}")
    print(f"Relevant Audit Events: {len(relevant_audit_events)}")
    print(f"Total Consent Events: {len(consent_logs)}")
    print(f"Relevant Consent Events: {len(relevant_consent_events)}")
    
    if relevant_audit_events and relevant_consent_events:
        print("\nCompliance passed: Relevant audit and consent data found.")
    else:
        print("\nCompliance failed: Missing relevant audit or consent data.")

def main():
    """Run the mock app."""
    # Simulate logging user actions and consent
    log_audit_event("John Doe", "accessed sensitive data")
    log_audit_event("Jane Smith", "accessed public data")

    log_consent_event("John Doe", "privacy policy")
    log_consent_event("Jane Smith", "terms of service")

    # Generate compliance report
    generate_compliance_report()

if __name__ == '__main__':
    main()
