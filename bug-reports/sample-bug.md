# Overview

This section outlines the bug reporting and retesting process designed using Jira. The goal is to ensure clear communication, traceability, and consistent defect lifecycle tracking between QA, developers, and BAs.

# Responsibility
- Designed bug report flow and defect lifecycle in Jira and Marker.io.
- Created custom templates for consistent bug and retest report formats.
- Designed and implemented SOPs to standardize bug titles, descriptions, terminology, and formatting in Jira to ensure consistency, clarity, and traceability across the QA team.

# Tools
- Jira
- Marker.io

# Example of bug report

- **Platform**: Jira
- **Custom Fields**: Environment, Priority, Linked Work Item, Assignee

## Functional bug

### Bug report: Incorrect Payment Type Displayed for Bank Account

| No. | Issue | Test Steps | Expected Result | Attachment |
|-----|-------|------------|-----------------|------------|
| 1   | In **Log Payment Management** page, the Payment Type for the Bank payment account is **incorrectly displayed as Emoney** instead of Bank. | 1. Update the payment account and select Bank as the account type. <br> 2. Navigate to Log Payment Management. <br> 3. Observe the Payment Type column for the updated account. | The Payment Type **should display as Bank** for Bank account. | SS_100.png|

**Note**: -

### Bug retest report:

| No. | Test Result | Attachment |
|-----|-------|------------|
| 1   | **Pass.** <br> The Payment Type **display as Bank** for Bank account.| RT_100.png|

## UI bug

### Bug report: Misaligned Button in Checkout Page

| No. | Issue | Test Steps | Expected Result | Attachment |
|-----|-------|------------|-----------------|------------|
| 1   | The **“Place Order” button is misaligned** and overlaps with the total price text on the **Checkout** page when viewed on smaller screen resolutions (e.g., 1024x768). | 1. Login to the website. <br> 2. Add any item to cart. <br> 3. Go to Checkout page. <br> 4. Resize browser window to 1024x768. <br> 5. Observe the button layout. | The “Place Order” button should be properly aligned below the total price and should not overlap, regardless of screen size. | SS_100.png |

**Notes:**
- Issue affects usability and may cause difficulty for users to complete a purchase on smaller screens.
- Tested on Chrome Version 123.0 and Firefox 115.0 on Windows 10.

### Bug retest report

| No. | Test Result | Attachment |
|-----|-------------|------------|
| 1   | **Pass**. <br> The “Place Order” button is now properly aligned below the total price and does not overlap on 1024x768 screen resolution. | RT_100.png |
