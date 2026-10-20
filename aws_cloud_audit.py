print("=== AWS CLOUD SECURITY AUDIT LAB ===")
print("Starting AWS security audit...")
security_checks = [
    "IAM permissions",
    "S3 Bucket security",
    "CloudTrail Logging",
    "Encryption Setting",
]
for checks in security_checks:
    print("[CHECK]", checks)
print("Initial audit checklist completed!")
print("\n=== IAM SECURITY AUDIT ===")
iam_users = [
    {"name": "admin_user", "mfa": True, "admin": True},
    {"name": "developer", "mfa": False, "admin": False},
    {"name": "test_user", "mfa": False, "admin": True}
]
for user in iam_users:
    print(f"\nchecking user: {user['name']}")
    if not user["mfa"]:
        print("[WARNING] MFA is disabled")
    else:
        print("[PASS] MFA is enable")
    if user["admin"]:
        print("[REVIEW] Adminastator access detected")
    else:
        print("[PASS] No administator access")
print("\n=== AWS S3 BUCKET SECURITY AUDIT ===")
s3_buckets = [
    {
        "name": "comapny-backup",
        "public_access": False,
        "encryption": True
    },
    {
        "name": "public-files",
        "public_access": True,
        "encryption": False
    },
    {
        "name": "employee-records",
        "public_access": False,
        "encryption": True
    }
]
for bucket in s3_buckets:
    print(f"\nchecking bucket: {bucket['name']}")
    print("DEBUG BUCKET:", bucket)
    if bucket["public_access"]:
        print("[WARNING] public access enabled")
    else:
        print("[PASS] public access disabled")
    if bucket["encryption"]:
        print("[PASS] Encryption enabled")
    else:
        print("[WARNING] Encryption disabled")
print("\nS3 Security Audit completed!")
print("\n=== AWS CLOUDTRAIL LOGGING AUDIT ===")
cloudtrail_logs = [
    {"name": "production-trail", "logging": True},
    {"name": "development-trail", "logging": False},
    {"name": "security-trail", "logging": True}
]
for trail in cloudtrail_logs:
    print(f"\nChecking trail: {trail['name']}")
    if trail["logging"]:
        print("[PASS] cloudTrail logging enabled")
    else:
        print("[WARNING] cloud trail logging disabled")
print("\nCloudTrail Audit completed!")
print("\n=== GENERATING AWS SECURITY REPORT ===")
findings = [
    "IAM: developer MFA disabled",
    "IAM: test_user MFA disabled",
    "IAM: Administator access requires review",
    "S3: public-files bucket has public access enabled",
    "S3: public-files bucket encryption disabled",
    "CloudTrail: development-trail logging disabled"
]
with open("aws_security_report.txt", "w", encoding="utf-8") as file:
    file.write("AWS CLOUD SECURITY AUDIT REPORT\n")
    file.write("=" * 40 + "\n")
    file.write("Audit Type: Simulated AWS Security audit\n\n")
    file.write("SECURITY FINDINGS\n")
    for number, finding in enumerate(findings, 1):
       file.write(f"{number}. {finding}\n")
    file.write("\nSECURITY RECOMMMENDATIONS\n")
    file.write("1. Enable MFA for IAM users.\n")
    file.write("2. Review administator permissions.\n")
    file.write("3. Restrict public S3 bucket access.\n")
    file.write("4. Enabled S3 bucket encryption.\n")
    file.write("5. Enabled CloudTrail logging.\n")
print("AWS Security report saved successfully!")


