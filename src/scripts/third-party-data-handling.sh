#!/bin/bash

CONSENT_LOG="src/logs/consent.log"

# Check if the consent log contains entries related to third-party services
if grep -qi "google analytics" "$CONSENT_LOG"; then
  echo "Consent for Google Analytics found. Third-party data handling check passed."
else
  echo "No consent for Google Analytics found. Third-party data handling check failed."
  exit 1
fi

# Check for Facebook Pixel consent
if grep -qi "facebook pixel" "$CONSENT_LOG"; then
  echo "Consent for Facebook Pixel found. Third-party data handling check passed."
else
  echo "No consent for Facebook Pixel found. Third-party data handling check failed."
  exit 1
fi

echo "Third-Party Data Handling Validation passed."


# testing: here