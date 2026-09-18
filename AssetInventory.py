# ============================================================
# CYBERSECURITY ASSET INVENTORY SYSTEM
# Weekly Mini Project - 01
# ============================================================

assets = []


# ------------------------------------------------------------
# ADD ASSET
# ------------------------------------------------------------
def add_asset():
    print("\n========== ADD ASSET ==========")

    asset_id = input("Enter Asset ID: ").strip()

    # Check duplicate ID
    for asset in assets:
        if asset["id"] == asset_id:
            print("Asset ID already exists!")
            return

    asset_name = input("Enter Asset Name: ").strip()

    print("\nAsset Types:")
    print("1. Workstation")
    print("2. Server")
    print("3. Router")
    print("4. Switch")
    print("5. Application")

    type_choice = input("Choose Asset Type: ")

    asset_types = {
        "1": "Workstation",
        "2": "Server",
        "3": "Router",
        "4": "Switch",
        "5": "Application"
    }

    if type_choice not in asset_types:
        print("Invalid Asset Type!")
        return

    asset_type = asset_types[type_choice]

    ip_address = input("Enter IP Address: ").strip()
    operating_system = input("Enter Operating System: ").strip()
    department = input("Enter Department: ").strip()

    print("\nRisk Levels:")
    print("1. Low")
    print("2. Medium")
    print("3. High")
    print("4. Critical")

    risk_choice = input("Choose Risk Level: ")

    risk_levels = {
        "1": "Low",
        "2": "Medium",
        "3": "High",
        "4": "Critical"
    }

    if risk_choice not in risk_levels:
        print("Invalid Risk Level!")
        return

    risk_level = risk_levels[risk_choice]

    print("\nSecurity Status:")
    print("1. Secure")
    print("2. Warning")
    print("3. Vulnerable")

    status_choice = input("Choose Security Status: ")

    statuses = {
        "1": "Secure",
        "2": "Warning",
        "3": "Vulnerable"
    }

    if status_choice not in statuses:
        print("Invalid Security Status!")
        return

    security_status = statuses[status_choice]

    asset = {
        "id": asset_id,
        "name": asset_name,
        "type": asset_type,
        "ip": ip_address,
        "os": operating_system,
        "department": department,
        "risk": risk_level,
        "status": security_status
    }

    assets.append(asset)

    print("\nAsset added successfully!")


# ------------------------------------------------------------
# DISPLAY ALL ASSETS
# ------------------------------------------------------------
def display_assets():
    print("\n========================================")
    print("      CYBERSECURITY ASSET INVENTORY")
    print("========================================")

    if len(assets) == 0:
        print("No assets available.")
        return

    for asset in assets:
        print("----------------------------------------")
        print("Asset ID       :", asset["id"])
        print("Asset Name     :", asset["name"])
        print("Asset Type     :", asset["type"])
        print("IP Address     :", asset["ip"])
        print("OS             :", asset["os"])
        print("Department     :", asset["department"])
        print("Risk Level     :", asset["risk"])
        print("Status         :", asset["status"])

    print("----------------------------------------")
    print("Total Assets   :", len(assets))


# ------------------------------------------------------------
# SEARCH ASSET
# ------------------------------------------------------------
def search_asset():
    print("\n========== SEARCH ASSET ==========")

    asset_id = input("Enter Asset ID to search: ").strip()

    for asset in assets:
        if asset["id"] == asset_id:
            print("\nAsset Found!")
            print("----------------------------------------")
            print("Asset ID       :", asset["id"])
            print("Asset Name     :", asset["name"])
            print("Asset Type     :", asset["type"])
            print("IP Address     :", asset["ip"])
            print("OS             :", asset["os"])
            print("Department     :", asset["department"])
            print("Risk Level     :", asset["risk"])
            print("Status         :", asset["status"])
            print("----------------------------------------")
            return

    print("Asset not found!")


# ------------------------------------------------------------
# UPDATE ASSET
# ------------------------------------------------------------
def update_asset():
    print("\n========== UPDATE ASSET ==========")

    asset_id = input("Enter Asset ID to update: ").strip()

    for asset in assets:
        if asset["id"] == asset_id:

            print("\nCurrent Asset Details:")
            print("Name       :", asset["name"])
            print("IP Address :", asset["ip"])
            print("OS         :", asset["os"])
            print("Department :", asset["department"])
            print("Risk       :", asset["risk"])
            print("Status     :", asset["status"])

            print("\nEnter new details.")
            print("Press Enter to keep the existing value.")

            new_name = input("Asset Name: ").strip()
            new_ip = input("IP Address: ").strip()
            new_os = input("Operating System: ").strip()
            new_department = input("Department: ").strip()

            if new_name:
                asset["name"] = new_name

            if new_ip:
                asset["ip"] = new_ip

            if new_os:
                asset["os"] = new_os

            if new_department:
                asset["department"] = new_department

            print("\nRisk Levels:")
            print("1. Low")
            print("2. Medium")
            print("3. High")
            print("4. Critical")
            print("Press Enter to keep existing risk.")

            risk_choice = input("Risk Level: ").strip()

            risk_levels = {
                "1": "Low",
                "2": "Medium",
                "3": "High",
                "4": "Critical"
            }

            if risk_choice in risk_levels:
                asset["risk"] = risk_levels[risk_choice]

            print("\nSecurity Status:")
            print("1. Secure")
            print("2. Warning")
            print("3. Vulnerable")
            print("Press Enter to keep existing status.")

            status_choice = input("Security Status: ").strip()

            statuses = {
                "1": "Secure",
                "2": "Warning",
                "3": "Vulnerable"
            }

            if status_choice in statuses:
                asset["status"] = statuses[status_choice]

            print("\nAsset updated successfully!")
            return

    print("Asset not found!")


# ------------------------------------------------------------
# DELETE ASSET
# ------------------------------------------------------------
def delete_asset():
    print("\n========== DELETE ASSET ==========")

    asset_id = input("Enter Asset ID to delete: ").strip()

    for asset in assets:
        if asset["id"] == asset_id:
            assets.remove(asset)
            print("Asset deleted successfully!")
            return

    print("Asset not found!")


# ------------------------------------------------------------
# RISK SUMMARY
# ------------------------------------------------------------
def risk_summary():
    print("\n========== RISK SUMMARY ==========")

    total = len(assets)

    critical = 0
    high = 0
    medium = 0
    low = 0
    vulnerable = 0

    for asset in assets:

        if asset["risk"] == "Critical":
            critical += 1

        elif asset["risk"] == "High":
            high += 1

        elif asset["risk"] == "Medium":
            medium += 1

        elif asset["risk"] == "Low":
            low += 1

        if asset["status"] == "Vulnerable":
            vulnerable += 1

    print("----------------------------------------")
    print("Total Assets      :", total)
    print("Critical Assets   :", critical)
    print("High Risk Assets  :", high)
    print("Medium Risk       :", medium)
    print("Low Risk Assets   :", low)
    print("Vulnerable Assets :", vulnerable)
    print("----------------------------------------")


# ------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------
def main():

    while True:

        print("\n")
        print("========================================")
        print("   CYBERSECURITY ASSET INVENTORY")
        print("========================================")
        print("1. Add Asset")
        print("2. Search Asset")
        print("3. Update Asset")
        print("4. Delete Asset")
        print("5. Display All Assets")
        print("6. Risk Summary")
        print("7. Exit")
        print("========================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_asset()

        elif choice == "2":
            search_asset()

        elif choice == "3":
            update_asset()

        elif choice == "4":
            delete_asset()

        elif choice == "5":
            display_assets()

        elif choice == "6":
            risk_summary()

        elif choice == "7":
            print("\nThank you for using Cybersecurity Asset Inventory System!")
            break

        else:
            print("\nInvalid choice! Please try again.")


# ------------------------------------------------------------
# PROGRAM START
# ------------------------------------------------------------
if __name__ == "__main__":
    main()