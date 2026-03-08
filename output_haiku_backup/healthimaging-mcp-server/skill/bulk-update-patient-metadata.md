---
name: bulk-update-patient-metadata
description: Update patient metadata across all studies for a patient.
---

# Bulk Update Patient Metadata

Update patient metadata across all studies for a patient.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | ID of the datastore |
| `patient_id` | string | Yes | DICOM Patient ID to update metadata for |
| `metadata_updates` | object | Yes | Patient metadata updates to apply across all studies |

