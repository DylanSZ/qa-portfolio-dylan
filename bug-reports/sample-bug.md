## Overview

This section outlines the bug reporting and retesting process designed using Jira. The goal is to ensure clear communication, traceability, and consistent defect lifecycle tracking between QA, developers, and BAs.

##Responsibility:
- Designed bug report flow and defect lifecycle in Jira.
- Created custom templates for consistent bug and retest report formats.

##Example of bug report:

- **Platform**: Jira
- **Custom Fields**: Environment, Priority, Linked Work Item, Assignee

Bug Report: Incorrect Payment Type Displayed for Bank Account

| No. | Issue | Test Steps | Expected Result | Attachment |
|-----|-------|------------|-----------------|------------|
| 1   | In **Log Payment Management** page, the Payment Type for the Bank payment account is **incorrectly displayed as Emoney** instead of Bank. | 1. Update the payment account and select Bank as the account type. <br> 2. Navigate to Log Payment Management. <br> 3. Observe the Payment Type column for the updated account. | The Payment Type **should display as Bank** for Bank account. | SS_100.png|

**Note**: -

##Example of bug retest report:

| No. | Test Result | Attachment |
|-----|-------|------------|
| 1   | **Pass.** <br> The Payment Type **display as Bank** for Bank account.| RT_100.png|


