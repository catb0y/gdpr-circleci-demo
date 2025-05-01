#!/bin/bash

CONSENT_LOG="src/logs/consent.log"

# Check if the consent log file contains withdrawal events (e.g., user withdrawal of consent)
if grep -q "withdrawn" "$CONSENT_LOG"; then
  echo "Consent withdrawal mechanism exists. Withdrawal check passed."
else
  echo "Consent withdrawal mechanism not found. Withdrawal check failed."
  exit 1
fi

echo "Consent Withdrawal Mechanism Check passed."
