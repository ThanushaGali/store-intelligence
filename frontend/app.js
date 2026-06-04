let brandChart = null;
let zoneChart = null;
async function loadDashboard() {

    const summary = await fetch(
        "http://127.0.0.1:8000/api/store-summary"
    );

    const revenue = await fetch(
        "http://127.0.0.1:8000/api/revenue"
    );

    const anomaly = await fetch(
        "http://127.0.0.1:8000/api/anomalies"
    );

    const journey = await fetch(
        "http://127.0.0.1:8000/api/customer-journeys"
    );

    const kpis = await fetch(
    "http://127.0.0.1:8000/api/kpis"
);



    const summaryData = await summary.json();
    const revenueData = await revenue.json();
    const anomalyData = await anomaly.json();
    const journeyData = await journey.json();
    const kpiData = await kpis.json();

    document.getElementById("lastUpdated").innerText =
    "Last Updated: " +
    new Date().toLocaleTimeString();

    document.getElementById("summary").innerHTML = `
        <div class="card">
            <h2>Footfall</h2>
                <p>${summaryData.footfall}</p>
    <span>Total Visitors</span>
        </div>

        <div class="card">
    <h2> Occupancy</h2>
    <p>${summaryData.occupancy}</p>
    <span>Current Store Count</span>
</div>

        <div class="card">
    <h2> Revenue</h2>
    <p>₹${summaryData.revenue}</p>
    <span>Total Sales</span>
</div>

        <div class="card">
            <h2>Top Brand</h2>
            <p>${summaryData.top_brand}</p>
        </div>

        <div class="card">
    <h2> Transactions</h2>
    <p>${summaryData.transactions}</p>
    <span>Completed Orders</span>
</div>

        <div class="card">
            <h2>Average Bill</h2>
            <p>₹${revenueData.average_bill.toFixed(2)}</p>
        </div>

        <div class="card">
            <h2>Anomalies</h2>
<p>
${
    anomalyData.anomalies.length > 0
    ? anomalyData.anomalies.join(", ")
    : "No Anomalies Detected"
}
</p>
        </div>

         <div class="card">
    <h2> Conversion Rate</h2>
    <p>${kpiData.conversion_rate}%</p>
    <span>Visitor Conversion</span>
</div>

    <div class="card">
    <h2> Revenue / Visitor</h2>
    <p>₹${kpiData.revenue_per_visitor}</p>
    <span>Revenue Efficiency</span>
</div>

    <div class="card">
        <h2>Most Visited Zone</h2>
        <p>${kpiData.most_visited_zone}</p>
    </div>

    `;

    let journeyHTML = "";

    for (const customer in journeyData) {
       journeyHTML += `
<div class="journey-card">

    <div class="journey-id">
        Customer #${customer}
    </div>

    <div class="journey-path">
        ${
            journeyData[customer]
            .map(zone => {
                if(zone === "Entry") return "🟢 Entrance";
                if(zone === "Exit") return "🔴 Exit";
                return zone;
            })
            .join(" → ")
        }
    </div>

</div>
`;
    }

    document.getElementById("journeys").innerHTML =
        journeyHTML;
}

    document.getElementById("heatmap").src =
    "http://127.0.0.1:8000/api/heatmap?t=" +
    Date.now();
loadDashboard();

setInterval(() => {
    loadDashboard();
}, 10000);

async function loadBrandChart() {

    const response = await fetch(
        "http://127.0.0.1:8000/api/revenue-by-brand"
    );

    const data = await response.json();
  


    const labels = Object.keys(data);
    const values = Object.values(data);

    if (brandChart) {
    brandChart.destroy();
}

brandChart = new Chart(
    document.getElementById("brandChart"),
    {
        type: "bar",
        data: {
            labels: labels,
            datasets: [{
                label: "Revenue",
                data: values
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    }
);
}



loadBrandChart();

async function loadZoneChart() {

    const response = await fetch(
        "http://127.0.0.1:8000/api/zones"
    );

    const data = await response.json();

    console.log("Zone Data:", data);
    const labels = [];
const values = [];

Object.entries(data).forEach(([zone, count]) => {

    if (count > 0) {

        labels.push(zone);
        values.push(count);

    }

});

    console.log("Zone API:", data);
    console.log("Labels:", labels);
    console.log("Values:", values);

    if (zoneChart) {
    zoneChart.destroy();
}

zoneChart = new Chart(
    document.getElementById("zoneChart"),
    {
        type: "doughnut",
        data: {
            labels: labels,
            datasets: [{
                data: values
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    }
);
}

loadZoneChart();

async function loadFunnel() {

    const response = await fetch(
        "http://127.0.0.1:8000/funnel"
    );

    const data = await response.json();

    document.getElementById(
    "funnel-container"
).innerHTML = `
    <div class="funnel-step">
        Entry: ${data.entry}
    </div>

    <div style="text-align:center;">↓</div>

    <div class="funnel-step">
        Zone Visit: ${data.zone_visit}
    </div>

    <div style="text-align:center;">↓</div>

    <div class="funnel-step">
        Billing: ${data.billing}
    </div>

    <div style="text-align:center;">↓</div>

    <div class="funnel-step">
        Purchase: ${data.purchase}
    </div>
`;
}
loadFunnel();

setInterval(() => {

    loadDashboard();
    loadFunnel();
    loadZoneChart();
    loadBrandChart();

}, 10000);

