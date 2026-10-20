# AWS-cloud-security-audit
A python-based simulated AWS Cloud security Audit tool designed to identify common cloud security misconfigurations and generate security assessment reports.
This project demonstrate practical cybersecurity auditing concepts relevant to Cloud security Analyst and SOC Analyst roles.
## Technologies Used
. Python 3
. AWS Security Concepts
. Identity and Access Managment(IAM)
. Amazon S3 Security
. AWS CloudTrial
. Visual studio code
. GitHub
## Security Audit Features
1. IAM security Audit
   . checks simulated IAM users for MFA status.
   . Identifies accounts with administrator privileges.
   . Flags excessive access for security review.
2. S3 Bucket Security Audit
   . Detects simulated publicly accessible S3 buckets.
   . Checks buckets encryption settings.
   . Identifies potential data exposure risks.
3. Security Reporting Generation
   . Generates an audit report automatically.
   . Documents security finidings.
   . Provides security recommendations.
## How To Run
1. Install python 3.
2. Download or clone this repository.
3. Open the project folder in VS code.
4. Run the following command:
   python aws_cloud_report.txt file.
5. Review the generated
  aws_security_report.txt file.
## Sample Security Findings
. MFA disabled for selected IAM users.
. Administrator permissions requiring review.
. Public S3 bucket access enabled.
. CloudTrail logging disabled.
## Skills Demonstrated
. Cloud security Assessment 
. Security Misconfiguration Detection 
. IAM Security Fundamentals
. Python Automation
. Security Reporting
. Risk identification 
. Security Best Practice 
## Disclaimer
This is an educational simulation using samples AWS configurations data. it does not connect to or audit a live AWS account.
## Future improvements 
. integrate  AWS Boto3 for authorized real AWS account assesments.
. add automated risk severity classification.
. export findings to JSON and CSV.
. implement additional AWS security checks.
