
Building a Service Bulletin Kit Tracker: Automating Upgrade Kit Management with Python & Streamlit
In industries like aviation, manufacturing, or any field dealing with heavy assets, service bulletins are a regular part of life. These documents outline required modifications, upgrades, or retrofits — which usually translate into specific kits made up of spare parts, equipment, and materials.

The typical manual workflow looks like this:

Read the bulletin and list out every required part and quantity
Check current inventory levels
Calculate what’s missing
Create a clean order list (usually in Excel)
Share updates with procurement, project managers, and sometimes clients
It’s repetitive, time-consuming, and prone to human error. So I decided to build a simple, focused tool to automate the core of this process.

What the Tool Does
This is a lightweight web app built entirely in Python using Streamlit. No complex backend, no fancy database — just something that gets the job done fast.

Here are the main capabilities:

Maintain Spare Parts Inventory
You can add or update stock levels for any part. Enter the part name (e.g., “Screw M5”, “Hydraulic Seal”, “Avionics Module”) and the quantity you’re adding or setting.

Define Kit Composition from a Service Bulletin
For any bulletin or upgrade, you assign a unique ID (e.g., “SB-2025-042” or “Retrofit-Project-X”). Then you add each required part and the exact quantity needed for that kit. This acts as a simple Bill of Materials (BOM) tied to the bulletin.

Instant Stock Availability Check
Enter the bulletin ID, and the tool immediately compares what’s required against current stock. It calculates shortages for every line item.

Visual Shortage Alerts
Any part that’s short shows up with a red highlight in the “Order Now” column — making it impossible to miss.

One-Click SAP-Ready Excel Export
With a single button click, you download a clean Excel file containing only the data needed for ordering:

Bulletin ID
Part name
Quantity needed
Current stock
Quantity to order
This file can be handed straight to procurement or uploaded into SAP MM for requisition creation.

Full Dashboard Overview
A dedicated page shows all defined kits and current stock levels in simple tables — great for quick status checks or sharing progress.

Step-by-Step: How to Use It
Let’s walk through a real example.

Step 1: Add Stock
Go to “Add Spare Parts” → Enter “Screw M5” and quantity 50 → Save.
Repeat for “Cable Assembly” (30 units) and “Gasket Kit” (12 units).

Step 2: Define a Kit
Go to “Define Kit (Bulletin)” → Bulletin ID: “SB-2025-042”
Add:

Screw M5 → 70 needed
Cable Assembly → 25 needed
Gasket Kit → 15 needed
Step 3: Generate the Report
Go to “Check & Order” → Enter “SB-2025-042” → Click “Generate Report”

You’ll see a table like:

Bulletin	Part	Needed	In Stock	Order Now
SB-2025-042	Screw M5	70	50	20
SB-2025-042	Cable Assembly	25	30	0
SB-2025-042	Gasket Kit	15	12	3
Rows with shortages are highlighted in red.

Step 4: Export for Procurement
Click “Download Excel for SAP” → File downloads instantly → Open it and forward to the team that raises purchase requisitions.

If everything is in stock, you get a success message instead — no unnecessary orders.

Tech Behind It
Streamlit: Turns Python scripts into interactive web apps with almost no frontend code
Pandas: Handles all the data manipulation and table display
SQLite: Lightweight built-in database (no setup needed)
Openpyxl: Generates proper Excel files
Everything runs locally or deployed for free on Streamlit Community Cloud.

Why This Is Useful
This tool cuts down hours of manual cross-checking into minutes. It reduces errors in ordering, gives instant visibility to stakeholders, and produces exactly the kind of clean output procurement teams need.

It’s deliberately simple — no over-engineering — because in real operations, reliability and speed matter more than flashy features.

Feel free to try the live version, fork the repo, or adapt it for your own workflows.

Live Demo: https://service-bulletin-kit-tracker-d7sk4zcvulguf5zthxlsej.streamlit.app/
