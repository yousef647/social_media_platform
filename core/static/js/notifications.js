// function fetchNotifications() {
//     fetch("/notifications/get/")
//         .then(response => response.json())
//         .then(data => {
//             data.notifications.forEach(notification => {
//                 alert(notification.message); // Replace with better UI
//             });
//         })
//         .catch(error => console.error("Error fetching notifications:", error));
// }
//
// if (window.location.pathname === "/") {
//     setInterval(fetchNotifications, 10000); // Poll every 10 seconds
// }