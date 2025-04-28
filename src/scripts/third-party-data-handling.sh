#!/bin/bash

# Mock third-party services (example: Google Analytics)
THIRD_PARTY_FILE="scripts/third_party_services.txt"

# Mock file contains services integrated into your app
# Example entries might include google-analytics, facebook-pixel, etc.
# Ensure that you have the mock file populated

# Check if the third-party service file exists
if [ ! -f "$THIRD_PARTY_FILE" ]; then
  echo "Error: $THIRD_PARTY_FILE not found."
  exit 1
fi

# Check if the third-party services list contains 'google-analytics'
if grep -q "google-analytics" "$THIRD_PARTY_FILE"; then
  echo "Third-party analytics found. Third-party data handling check passed."
else
  echo "Third-party analytics not found. Third-party data handling check failed."
  exit 1
fi

# Check for other common third-party services
if grep -q "facebook-pixel" "$THIRD_PARTY_FILE"; then
  echo "Facebook Pixel found. Third-party data handling check passed."
else
  echo "Facebook Pixel not found. Third-party data handling check failed."
  exit 1
fi

echo "Third-Party Data Handling Validation passed."
