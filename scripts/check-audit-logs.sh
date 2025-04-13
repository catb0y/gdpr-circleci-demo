#!/bin/bash

AUDIT_LOG="logs/audit.log"

# Check if the audit log contains entries related to sensitive data access
if grep -q "sensitive" "$AUDIT_LOG"; then
  echo "Audit log contains sensitive data access. Audit check passed."
  exit 0
else
  echo "Audit log does not contain sensitive data access. Audit check failed."
  exit 1
fi
