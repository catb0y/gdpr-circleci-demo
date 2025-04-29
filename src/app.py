import os
import time

# Paths to logs 
logs_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
audit_log_file = os.path.join(logs_directory, 'audit.log')
consent_log_file = os.path.join(logs_directory, 'consent.log')

# Additional logs
withdrawal_mechanism_log = os.path.join(logs_directory, 'consent_banner_check.log')
third_party_analytics_log = os.path.join(logs_directory, 'third_party_analytics.log')


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

def log_verify_withdrawal_mechanism(user, consent_type):
    """Log a consent withdrawal event."""
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
    log_entry = f'{timestamp} - {user} withdrawn consent for {consent_type}\n'
    
    with open(consent_log_file, 'a') as log_file:
        log_file.write(log_entry)
    print(f"Consent withdrawal logged: {log_entry.strip()}")

def log_third_party_analytics_check():
    """Log a third-party analytics check."""
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
    log_entry = f'{timestamp} - Third-party analytics check passed\n'
    
    with open(third_party_analytics_log, 'a') as log_file:
        log_file.write(log_entry)
    print(f"Third-party analytics check logged: {log_entry.strip()}")

def main():
    """Run the mock app."""
    # Simulate logging user actions and consent
    log_audit_event("John Doe", "accessed sensitive data")
    log_audit_event("Jane Smith", "accessed public data")

    log_consent_event("John Doe", "privacy policy")
    log_consent_event("Jane Smith", "terms of service")
    log_consent_event("John Doe", "Google Analytics") # here
    log_consent_event("John Doe", "Facebook Pixel") # here
    
    # Simulate the consent banner and third-party analytics checks
    log_verify_withdrawal_mechanism("John Doe", "privacy policy")
    log_third_party_analytics_check()

if __name__ == '__main__':
    main()
