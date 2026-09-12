# Function Space

- **Source URL:** `https://help.ideasrms.com/g3rms_cp/Content/Function-Space/Function-Space.htm`
- **Breadcrumb:** `Home`
- **Topic Path:** `Content/Function-Space/Function-Space.htm`
- **Ingestion Date:** `2026-09-11 22:12:22`

---

# Function Space

Function Space allows you to apply the revenue optimization strategies from guest rooms to your function rooms. Function Space forecasts future demand, helps you make better decisions about the status of function-only business, and lets you evaluate groups so that you can decide whether to accept them and at what price.
IfG3 RMSintegrates with theDelphisales and catering system,  you can start evaluations in Delphi.

### What Help Do You Need with Function Space?

- I wantan overviewon how Function Space can help maximize profits.
- I want toset up Function Space.
- I want to learn which features to use whenmanaging Function Space.
- I want to understand howG3 RMSusesspace, profit, and timeto calculate its metrics.
- I want to understandFunction Space metricslike ProPAST.
View this video or read the overview below.
Your browser does not support the video tag.
- Function Space identifies  function room demand patterns and forecasts future demand, with the goal of maximizing overall function room profit.
- Function Space also helps you make better decisions about the status of function-only business opportunities. Use the forecast of low and high demand to decide when to save function rooms for groups with guest rooms and when to release function rooms to function-only business.
- You can also use Function Space to evaluate group opportunities. Enter the details about a potential group booking, then use the results to understand the group's profit contribution and to decide whether to accept the group and at which price.

#### Dashboard

TheDashboarddisplays key performance metrics that help you understand the patterns and trends of your Function Space business.

#### Demand Calendar

Demand Calendar: View a monthly summary of function space demand, review forecasts, drill down to daily details,  and compare to last year's information.
Ensure that you understand thefunction space metricslike ProPOST, which differ from guest room metrics.

#### Evaluations

New Evaluation:Input prospective group details and complete an evaluation for multiple potential arrival dates.
Evaluation Results: View the high-level results of an evaluation.
Evaluation Details: Drill down into the details of an evaluation for each potential group arrival date.
Adjust Evaluation Results: Adjust the weighting of revenue sources from a group to develop a contract that takes advantage of available profit margins.

#### Forecast Review

Forecast Review: Review the Function Space utilization forecast by day and Day Part.
Forecast Overrides: Override the system's utilization forecast.
Function Only Business Status: Set the sell status for function-only business at the day or Day Part level.

#### Performance Trends

Performance Trendsallows you to analyze historical function space performance and future demand. You can view Function Space Utilization, Revenue, Profit, and more detailed data at the day and Day Part level.

#### Configuration

Servicing Cost: Define the Per Room Servicing Cost for guest rooms and measurement preference for function rooms.
Conference & Banquet: Set up the profit percentage  that your property generates from each conference and banquet revenue stream thatG3 RMSimports from your sales and catering system, for use in evaluations.
Ancillary: Define the Ancillary Revenue Streams, like restaurant or spa, together with their profit percentage, as well as assign expected ancillary revenue by market segment  to improve the system's transient displacement analysis.
Day Parts: Define the portions of the day forG3 RMSto use for forecasting.
Function Rooms: Select the function rooms that you wantG3 RMSto revenue manage, define their price tier and their price range.
Group Status: If your property has aDelphi integration, use this tab to define the behavior of the Delphi codes.
Forecast Levels: Define the percentage of utilization at which you consider function space usage to be low, medium or high.
Event Types: Define the types of events that represent periods when function rooms are not available for sale, for example, Out of Service.
Market Segment: Map your sales and catering market segments to yourG3 RMSmarket segments.
Package: If you use per attendee (or daily delegate) pricing, define the packages that you offer to groups.
Guest Room Type: Map your sales and catering room types to yourG3 RMSroom types.
Room Type: Designate which room types you use for group business.
Base Room Type: Select the Base Room Type for each Room Class, which is the guest room type on whichG3 RMSbases its pricing for each Room Class.
Ceiling/Floor: Define the highest and lowest guest room prices that you would charge in an  evaluation.
Offsets: Set up guest room prices for different room types within a Room Class using offsetting from the Base Room Type value.

## Function Space Metrics

### Space

Space refers to the function rooms that are set as Include inFunction Rooms configuration.G3 RMSmeasures function rooms by their square area in either meters or feet, based on yourpreference. The system considers each indivisible portion of a function room, because you might sell the entire function room or its separate parts.

### Profit

G3 RMSmeasures both revenue and profit, but it uses profit for evaluations because the different revenue streams (food, meeting room rental, etc.) have different profit contributions.
For example, two group inquire about the same space and time and have equal guest room needs. One group has $900 in banquet food and no meeting room rental, the other only $800 in room rental. The $800 group has lower revenue but is likely the better, more profitable, choice, due to the usually much higher profit % of room rental versus banquet food. Measuring profit enables the system to understand the true value of a group.

### Time

G3 RMSmeasures time by hours in a Day Part. A Day Part is a block of time during which an event can take place, including its set up and tear down time. TheDay Parts configuredby default are Morning, Noon, Afternoon, Evening, and Overnight.
- Day Parts are for  measuring utilization and don't limit when events occur. Events can fall within a Day Part or span multiple Day Parts.
- Utilization of a Day Part and function room is either 0% or 100%. If one Day Part contains two separate events, the system considers that Day Part as 100% utilized (not 200%), but uses the revenue from both events. If an event spans two Day Parts, the system considers both Day Parts 100% utilized.
For all metrics, Area refers to the square area and Time to the hours of all Day Parts that are available or utilized. Reviewhow Day Parts define timefor all metrics.

### Function Space Utilization

Function Space Utilization is similar to occupancy for guest rooms. It's a percentage that shows how much of your function space is booked:

#### Revenue Producing Utilization Only

The calculation of thisDashboardmetric uses Utilized Function Space only if it included revenues.

### Function Space Efficiency

Function Space Efficiency measures the percentage of Function Space Utilization that generates revenues. It compares Function Space Utilization to Revenue Producing Utilization Only.

### Profit per Available Space Time (ProPAST)

ProPAST is similar toRevPARRevenue Per Available Room. The total room revenue divided by the total number of rooms (capacity).
See the Property Information topic for the capacity definition.for guest rooms and measures how efficiently you use your function space. For example, ProPAST decreases if the time for set up and tear down of events increases. ProPAST also shows which rooms are driving your function revenue, helping you decide for which functions rooms to charge more or less.
To calculate ProPAST, we first combine all revenue streams  (banquet food, beverage, room hire, guest rooms, etc.) for the Day Part. Then we apply the configured Profit % to each revenue stream to calculate the profit. Finally, we divide the profit by the available function space.
Note: ProPAST and ProPOST are measured by the square meter or foot.  Depending on how much space you measure, these values might be very small. And increasing that value by a few cents could mean increasing profits by thousands for a month. Thus, use these values as a baseline to monitor your profit trends.

### Profit per Occupied Space Time (ProPOST)

ProPOST is similar to ADR for guest rooms. It measures how much profit you generate from your occupied function space. The calculation is similar to ProPAST; the only difference is that you divide by the occupied (or utilized) instead of available function space.

### Revenue per Available Space Time (RevPAST)

RevPAST is similar to ProPAST but uses revenue instead of profit. Compare the two metrics to see which function space business is most profitable.

### Revenue per Occupied Space Time (RevPOST)

RevPOST is similar to ProPOST but uses revenue instead of profit. Compare the two metrics to see which function space business is most profitable.
