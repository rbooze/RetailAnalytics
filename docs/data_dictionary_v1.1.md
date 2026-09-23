### Dimension Tables

#### DimChannel
* **Purpose:** Sales channel analysis.
* **Grain:** One row per source.

| Column | Data Type | Description |
| :--- | :--- | :--- |
| `ChannelKey` | INT | Channel key |
| `ChannelID` | INT | Business identifier |
| `ChannelName` | VARCHAR | Channel name |

#### DimCustomer
* **Purpose:** Customer profile and segmentation.
* **Grain:** One row per customer.

| Column | Data Type | Description |
| :--- | :--- | :--- |
| `CustomerKey` | INT | Customer key |
| `CustomerID` | INT | Business identifier |
| `FirstName` | VARCHAR | Customer first name |
| `LastName` | VARCHAR | Customer last name |
| `State` | VARCHAR | Customer state |
| `Segment` | VARCHAR | Customer segment |
| `JoinDate` | DATE | Account creation date |

* **Segments:**
  * **Budget:** Discount-focused
  * **Casual:** Occasional buyer
  * **Enthusiast:** Frequent outdoor buyer
  * **Professional:** Business purchases
  * **VIP:** Highest value customers

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
| `Day` | INT | Day of month |
| `DayName` | VARCHAR | Day name |

* **Used for:**
  * YoY growth
  * Monthly trends
  * Seasonal analysis

#### DimProduct
* **Purpose:** Product catalog.
* **Grain:** One row per product.

| Column | Data Type | Description |
| :--- | :--- | :--- |
| `ProductKey` | INT | Product key |
| `ProductID` | INT | Product identifier |
| `ProductName` | VARCHAR | Product description |
| `Category` | VARCHAR | Product category |
| `Subcategory` | VARCHAR | Product grouping |
| `SupplierID` | INT | Product supplier |
| `Cost` | DECIMAL | Product cost |
| `Price` | DECIMAL | Selling price |
| `ProductStatus` | VARCHAR | Active/discontinued |

* **Categories:** Apparel, Camping, Fishing, Footwear, Hiking, Kayaking
* **Subcategories:** Backpacks, Hiking Boots, Jackets, Kayaks, Lighting, Paddles, Reels, Rods, Shirts,
                     Sleeping Bags, Tents, Trail Shoes, Trekking Poles

#### DimPromotion
* **Purpose:** Marketing campaign analysis.
* **Grain:** One row per promotion.

| Column | Data Type | Description |
| :--- | :--- | :--- |
| `PromotionKey` | INT | Promotion key |
| `PromotionID` | INT | Campaign identifier |
| `CampaignName` | VARCHAR | Campaign name |
| `CampaignType` | VARCHAR | Promotion category |
| `DiscountPercent` | DECIMAL | Discount offered |
| `TestGroup` | VARCHAR | A/B test group |
| `TargetSegment` | VARCHAR | Target Group |
| `CategoryTarget` | VARCHAR | Category Group |

* **Examples:** `SPRING15`, `CAMP25`, `VIP10`, `BLACKFRIDAY40`

#### DimSupplier
* **Purpose:** Supplier performance analysis.
* **Grain:** One row per supplier.

| Column | Data Type | Description |
| :--- | :--- | :--- |
| `SupplierKey` | INT | Supplier key |
| `SupplierID` | INT | Supplier identifier |
| `SupplierName` | VARCHAR | Supplier name |
| `Country` | VARCHAR | Supplier location |
| `SupplierTier` | VARCHAR | Strategic classification |
| `LeadTimeDays` | INT | Average delivery time |
| `QualityScore` | DECIMAL | Supplier quality rating |
| `RiskLevel` | VARCHAR | Supplier risk rating |

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

---

### Fact Tables

#### FactCustomerExperiment
* **Purpose:** Store outcome of a marketing A/B test at the individual customer level.
* **Grain:** One row per Customer per Experiment.

| Column | Data Type | Description |
|---------|-----------|-------------|
| ExperimentID | INT | Experiment identifier |
| CustomerID | INT | Business identifier |
| GroupName | VARCHAR(20) | Group name |
| PromotionID | INT | Campaign identifier |
| StartDate | DATE | Start of experiment |
| EndDate | DATE | End of experiment |
| Purchased | BIT | Customer made a purchase (1 = Yes, 0 = No) |
| PurchaseDate | DATE | Purchase date, if applicable |
| Revenue | DECIMAL(12,2) | Revenue |
| Profit | DECIMAL(12,2) | Profit |
| Returned | BIT | Purchased item returned (1 = Yes, 0 = No) |
| ReturnAmount | DECIMAL(12,2) | Dollar amount refunded |
| PurchaseDateKey | INT | Purchase key |

#### FactSales
* **Purpose:** Core sales transaction table.
* **Grain:** One row per product purchased per order.

| Column | Description |
| :--- | :--- |
| `SalesKey` | INT | Transaction key |
| `OrderID` | INT | Order identifier |
| `DateKey` | INT | Sale date |
| `CustomerKey` | INT | Buyer |
| `ProductKey` | INT | Product purchased |
| `PromotionKey` | INT | Discount campaign |
| `ChannelKey` | INT | Sales channel |
| `WarehouseKey` | INT | Fulfillment location |
| `Quantity` | INT | Units sold |
| `SalesAmount` | DECIMAL | Revenue |
| `CostAmount` | DECIMAL | Product cost |
| `DiscountAmount` | DECIMAL | Discount value |
| `ProfitAmount` | DECIMAL | Revenue - Cost |

* **Business KPIs:** Revenue, Gross Profit, Margin %, Average Order Value, Units Sold

### Staging Tables
#### StagingChannel
* **Purpose:** Sales channel analysis.
* **Grain:** One row per source.

| Column | Data Type | Description |
| :--- | :--- | :--- |
| `ChannelID` | INT | Business identifier |
| `ChannelName` | VARCHAR | Channel name |

#### StagingCustomer
* **Purpose:** Customer profile and segmentation.
* **Grain:** One row per customer.

| Column | Data Type | Description |
| :--- | :--- | :--- |
| `CustomerID` | INT | Business identifier |
| `FirstName` | VARCHAR | Customer first name |
| `LastName` | VARCHAR | Customer last name |
| `State` | VARCHAR | Customer state |
| `Segment` | VARCHAR | Customer segment |
| `JoinDate` | DATE | Account creation date |

* **Segments:**
  * **Budget:** Discount-focused
  * **Casual:** Occasional buyer
  * **Enthusiast:** Frequent outdoor buyer
  * **Professional:** Business purchases
  * **VIP:** Highest value customers

#### StagingDates
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
| `Day` | INT | Day of month |
| `DayName` | VARCHAR | Day name |

#### StagingExperimentResults
* **Purpose:** Temporarily stores customer-level A/B test results generated by the Python ETL process.
* **Grain:** One row per Customer per Experiment.

| Column | Data Type | Description |
| :--- | :--- | :--- |
| `CustomerID` | INT | Product identifier |
| `Purchased` | BIT | Product purchased (1 = Yes, 0 = No) |
| `PurchaseDate` | DATE | Purchase date |
| `Revenue` | DECIMAL | Revenue |
| `Profit` | DECIMAL | Profit |

#### StagingProduct
* **Purpose:** Product catalog.
* **Grain:** One row per product.

| Column | Data Type | Description |
| :--- | :--- | :--- |
| `ProductID` | INT | Product identifier |
| `ProductName` | VARCHAR | Product description |
| `Category` | VARCHAR | Product category |
| `Subcategory` | VARCHAR | Product grouping |
| `SupplierID` | INT | Product supplier |
| `Cost` | DECIMAL | Product cost |
| `Price` | DECIMAL | Selling price |
| `ProductStatus` | VARCHAR | Active/discontinued |

* **Categories:** Apparel, Camping, Fishing, Footwear, Hiking, Kayaking
* **Subcategories:** Backpacks, Hiking Boots, Jackets, Kayaks, Lighting, Paddles, Reels, Rods, Shirts,
                     Sleeping Bags, Tents, Trail Shoes, Trekking Poles

#### StagingPromotion
* **Purpose:** Marketing campaign analysis.
* **Grain:** One row per promotion.

| Column | Data Type | Description |
| :--- | :--- | :--- |
| `PromotionID` | INT | Campaign identifier |
| `CampaignName` | VARCHAR | Campaign name |
| `CampaignType` | VARCHAR | Promotion category |
| `DiscountPercent` | DECIMAL | Discount offered |
| `TestGroup` | VARCHAR | A/B test group |
| `TargetSegment` | VARCHAR | Target Group |
| `CategoryTarget` | VARCHAR | Category Group |

* **Examples:** `SPRING15`, `CAMP25`, `VIP10`, `BLACKFRIDAY40`

#### StagingSales
* **Purpose:** Core sales transaction table.
* **Grain:** One row per product purchased per order.

| Column | Description |
| :--- | :--- |
| `SalesID` | INT | Transaction identifier |
| `OrderID` | INT | Order identifier |
| `DateKey` | INT | Sale date |
| `CustomerID` | INT | Buyer identifier |
| `ProductID` | INT | Product identifier |
| `ChannelID` | INT | Sales channel |
| `WarehouseID` | INT | Fulfillment location |
| `Quantity` | INT | Units sold |
| `SalesAmount` | DECIMAL | Revenue |
| `CostAmount` | DECIMAL | Product cost |
| `DiscountAmount` | DECIMAL | Discount value |
| `ProfitAmount` | DECIMAL | Revenue - Cost |

* **Business KPIs:** Revenue, Gross Profit, Margin %, Average Order Value, Units Sold

#### StagingSupplier
* **Purpose:** Supplier performance analysis.
* **Grain:** One row per supplier.

| Column | Data Type | Description |
| :--- | :--- | :--- |
| `SupplierID` | INT | Supplier identifier |
| `SupplierName` | VARCHAR | Supplier name |
| `Country` | VARCHAR | Supplier location |
| `SupplierTier` | VARCHAR | Strategic classification |
| `LeadTimeDays` | INT | Average delivery time |
| `QualityScore` | DECIMAL | Supplier quality rating |
| `CostRating` | VARCHAR | Supplier cost rating |
| `RiskLevel` | VARCHAR | Supplier risk rating |

#### StagingWarehouse
* **Purpose:** Distribution center analysis.
* **Grain:** One row per warehouse.

| Column | Data Type | Description |
| :--- | :--- | :--- |
| `WarehouseID` | INT | Warehouse identifier |
| `WarehouseName` | VARCHAR | Warehouse name |
| `Region` | VARCHAR | Location |
| `Capacity` | INT | Storage capacity |

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
