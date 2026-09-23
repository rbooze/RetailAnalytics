# Blue Ridge Outfitters Analytics Platform
## Data Dictionary v1.1

### 1. Business Overview

* **Company:** Blue Ridge Outfitters
* **Industry:** Outdoor Retail
* **Purpose:** Analyze sales, profitability, customers, inventory, suppliers, marketing performance, and operational efficiency.

#### Primary Business Questions

| Area | Question |
| :--- | :--- |
| **Sales** | What products and categories drive revenue? |
| **Finance** | Why is profit increasing or declining? |
| **Customers** | Which customers are most valuable? |
| **Marketing** | Which campaigns generate profitable growth? |
| **Inventory** | What products risk stockouts? |
| **Suppliers** | Which suppliers impact cost and quality? |
| **Operations** | Where are fulfillment problems occurring? |

---

### 2. Data Warehouse Design

We will use a star schema.

#### Dimensions
Dimensions describe the business.
* `DimDate`
* `DimCustomer`
* `DimProduct`
* `DimSupplier`
* `DimPromotion`
* `DimWarehouse`
* `DimChannel`
* `DimRegion`

#### Fact Tables
Facts record events.
* `FactSales`
* `FactReturns`
* `FactInventory`
* `FactShipments`
* `FactMarketing`
* `FactWebsiteSessions`

---

### 3. Dimension Tables

#### DimDate
* **Purpose:** Provides calendar intelligence for reporting.
* **Grain:** One row per calendar day.

| Column | Data Type | Description |
| :--- | :--- | :--- |
| `DateKey` | INT | Surrogate date key YYYYMMDD |
| `FullDate` | DATE | Calendar date |
| `Year` | INT | Calendar year |
| `Quarter` | INT | Quarter number |
| `Month` | INT | Month number |
| `MonthName` | VARCHAR | Month description |
| `Week` | INT | Week number |
| `Day` | INT | Day of month |
| `DayName` | VARCHAR | Day name |
| `IsWeekend` | BIT | Weekend indicator |

* **Used for:**
  * YoY growth
  * Monthly trends
  * Seasonal analysis

#### DimCustomer
* **Purpose:** Customer profile and segmentation.
* **Grain:** One row per customer.

| Column | Data Type | Description |
| :--- | :--- | :--- |
| `CustomerKey` | INT | Warehouse key |
| `CustomerID` | INT | Business identifier |
| `FirstName` | VARCHAR | Customer first name |
| `LastName` | VARCHAR | Customer last name |
| `State` | VARCHAR | Customer state |
| `RegionKey` | INT | Geographic region |
| `Segment` | VARCHAR | Customer segment |
| `JoinDate` | DATE | Account creation date |
| `LifetimeValueTier` | VARCHAR | Customer value category |

* **Segments:**
  * **Budget:** Discount-focused
  * **Casual:** Occasional buyer
  * **Enthusiast:** Frequent outdoor buyer
  * **Professional:** Business purchases
  * **VIP:** Highest value customers

#### DimProduct
* **Purpose:** Product catalog.
* **Grain:** One row per product.

| Column | Data Type | Description |
| :--- | :--- | :--- |
| `ProductKey` | INT | Warehouse key |
| `ProductID` | INT | Product identifier |
| `ProductName` | VARCHAR | Product description |
| `Category` | VARCHAR | Product category |
| `Subcategory` | VARCHAR | Product grouping |
| `SupplierKey` | INT | Product supplier |
| `Cost` | DECIMAL | Product cost |
| `Price` | DECIMAL | Selling price |
| `LaunchDate` | DATE | Product introduction |
| `ProductStatus` | VARCHAR | Active/discontinued |

* **Categories:** Camping, Hiking, Fishing, Climbing, Apparel, Footwear, Cycling, Kayaking

#### DimSupplier
* **Purpose:** Supplier performance analysis.
* **Grain:** One row per supplier.

| Column | Data Type | Description |
| :--- | :--- | :--- |
| `SupplierKey` | INT | Warehouse key |
| `SupplierID` | INT | Supplier identifier |
| `SupplierName` | VARCHAR | Supplier name |
| `Country` | VARCHAR | Supplier location |
| `LeadTimeDays` | INT | Average delivery time |
| `QualityScore` | DECIMAL | Supplier quality rating |
| `SupplierTier` | VARCHAR | Strategic classification |

#### DimPromotion
* **Purpose:** Marketing campaign analysis.
* **Grain:** One row per promotion.

| Column | Data Type | Description |
| :--- | :--- | :--- |
| `PromotionKey` | INT | Warehouse key |
| `PromotionID` | INT | Campaign identifier |
| `CampaignName` | VARCHAR | Campaign name |
| `DiscountPercent` | DECIMAL | Discount offered |
| `StartDate` | DATE | Campaign start |
| `EndDate` | DATE | Campaign end |
| `CampaignType` | VARCHAR | Promotion category |
| `TestGroup` | VARCHAR | A/B test group |

* **Examples:** `SPRING15`, `CAMP25`, `VIP10`, `BLACKFRIDAY40`

#### DimWarehouse
* **Purpose:** Distribution center analysis.
* **Grain:** One row per warehouse.

| Column | Data Type | Description |
| :--- | :--- | :--- |
| `WarehouseKey` | INT | Warehouse key |
| `WarehouseID` | INT | Warehouse identifier |
| `WarehouseName` | VARCHAR | Warehouse name |
| `Region` | VARCHAR | Location |
| `Capacity` | INT | Storage capacity |

#### DimChannel
* **Purpose:** Sales channel analysis.

| Column | Description |
| :--- | :--- |
| `ChannelKey` | Warehouse key |
| `ChannelName` | Store, Website, Mobile App |

---

### 4. Fact Tables

#### FactSales
* **Purpose:** Core sales transaction table.
* **Grain:** One row per product purchased per order.

| Column | Description |
| :--- | :--- |
| `SalesKey` | Transaction key |
| `OrderID` | Order identifier |
| `DateKey` | Sale date |
| `CustomerKey` | Buyer |
| `ProductKey` | Product purchased |
| `PromotionKey` | Discount campaign |
| `ChannelKey` | Sales channel |
| `WarehouseKey` | Fulfillment location |
| `Quantity` | Units sold |
| `SalesAmount` | Revenue |
| `CostAmount` | Product cost |
| `DiscountAmount` | Discount value |
| `ProfitAmount` | Revenue - Cost |

* **Business KPIs:** Revenue, Gross Profit, Margin %, Average Order Value, Units Sold

#### FactReturns
* **Purpose:** Analyze product quality.
* **Grain:** One row per returned item.

| Column | Description |
| :--- | :--- |
| `ReturnKey` | Return identifier |
| `OrderID` | Original order |
| `ProductKey` | Returned product |
| `CustomerKey` | Customer |
| `ReturnDate` | Return date |
| `Reason` | Return reason |
| `RefundAmount` | Amount refunded |

* **Return Reasons:** Defective, Wrong Size, Customer Changed Mind, Late Delivery, Damaged

#### FactInventory
* **Purpose:** Inventory management.
* **Grain:** One row per product per warehouse per day.

| Column | Description |
| :--- | :--- |
| `InventoryKey` | Identifier |
| `DateKey` | Date |
| `ProductKey` | Product |
| `WarehouseKey` | Warehouse |
| `QuantityOnHand` | Inventory available |
| `ReorderPoint` | Minimum stock |
| `StockoutFlag` | Out of stock |

* **KPIs:** Inventory Turns, Days On Hand, Stockout Rate

#### FactMarketing
* **Purpose:** Campaign performance.
* **Grain:** One row per campaign per day.

| Column | Description |
| :--- | :--- |
| `MarketingKey` | Identifier |
| `DateKey` | Date |
| `PromotionKey` | Campaign |
| `Spend` | Marketing cost |
| `Impressions` | Views |
| `Clicks` | Engagement |
| `Conversions` | Purchases |

* **KPIs:** Conversion Rate, CAC, ROAS

#### FactWebsiteSessions
* **Purpose:** Digital funnel analysis.
* **Grain:** One row per website session.

| Column | Description |
| :--- | :--- |
| `SessionKey` | Session ID |
| `DateKey` | Date |
| `CustomerKey` | Customer |
| `ChannelKey` | Source |
| `Device` | Desktop/mobile |
| `PagesViewed` | Engagement |
| `AddedToCart` | Cart activity |
| `Purchased` | Conversion |

---

### 5. Relationships

```text
                 DimDate
                    |
                    |
DimCustomer ---- FactSales ---- DimProduct
                    |               |
             DimPromotion      DimSupplier
                    |
              DimChannel
                    |
             DimWarehouse
DimProduct
      |
DimSupplier

---

#### Supporting models:

DimProduct
      |
FactInventory
      |
DimWarehouse


DimProduct
      |
FactReturns
      |
DimCustomer

### 6. Business Value & Insights Enabled
* Sales: "Why did revenue change?"  
* Profitability: "Are discounts hurting margins?"  
* Customers: "Which segment creates the most profit?"  
* Marketing: "Did Campaign A beat Campaign B?"  
* Suppliers: "Is supplier quality impacting returns?"  
* Inventory: "Why are we losing sales?"