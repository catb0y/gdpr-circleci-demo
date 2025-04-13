#!/bin/bash

CONSENT_LOG="src/logs/consent.log"

# Check if the consent log contains  entries related to privacy policy consent
if grep -q "privacy" "$CONSENT_LOG"; then
  echo "Consent log contains privacy policy consent. Consent check passed."
  exit 0
else
  echo "Consent log does not contain privacy policy consent. Consent check failed."
  exit 1
fi
