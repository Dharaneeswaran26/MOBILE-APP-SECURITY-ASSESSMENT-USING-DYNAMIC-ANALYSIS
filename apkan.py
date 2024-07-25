from androguard.core.bytecodes.apk import APK

apk_path = "CLIENT.apk"  # Replace with your APK file path

# Load the APK file
apk = APK(apk_path)

# Print some basic information
print(f"App Name: {apk.get_app_name()}")
print(f"Package: {apk.get_package()}")
print(f"Main Activity: {apk.get_main_activity()}")

def check_trustworthiness(apk_file):
    apk = APK(apk_file)

    # Check permissions
    permissions = apk.get_permissions()
    print("\nPermissions:")
    for permission in permissions:
        print(permission)

    # Check activities
    activities = apk.get_activities()
    print("\nActivities:")
    for activity in activities:
        print(activity)

    # Check receivers
    receivers = apk.get_receivers()
    print("\nReceivers:")
    for receiver in receivers:
        print(receiver)

    # Check services
    services = apk.get_services()
    print("\nServices:")
    for service in services:
        print(service)

    # Additional checks can be added based on specific security concerns
apk_file = "smsware.apk"
check_trustworthiness(apk_file)