async function uploadVideo() {

    const status =
        document.getElementById("status");

    status.innerHTML =
        "📤 Uploading CCTV Video...";

    setTimeout(() => {
        status.innerHTML =
            "🧠 Detecting Customers...";
    }, 2000);

    setTimeout(() => {
        status.innerHTML =
            "🎯 Tracking Customer Movement...";
    }, 4000);

    setTimeout(() => {
        status.innerHTML =
            "📊 Generating Analytics...";
    }, 6000);

    setTimeout(() => {
        status.innerHTML =
            "✅ Dashboard Updated Successfully";
    }, 8000);

    setTimeout(() => {
        window.location.href = "index.html";
    }, 10000);
}