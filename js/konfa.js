document.addEventListener('DOMContentLoaded', function() {
    // Countdown Timer
    const countdownElement = document.getElementById('countdown');
    const conferenceDate = new Date('2024-09-01T12:00:00'); // Example date
    const updateCountdown = () => {
        const now = new Date();
        const timeDifference = conferenceDate - now;
        const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);
        countdownElement.textContent = `${days}d ${hours}h ${minutes}m ${seconds}s`;
    };
    setInterval(updateCountdown, 1000);

    // Add to Calendar Function
    window.addToCalendar = function() {
        alert('Add to Calendar functionality coming soon!');
    };

    // Book a Seat Function
    window.bookSeat = function() {
        alert('Book a Seat functionality coming soon!');
    };
});