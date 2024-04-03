
// Counter for Projects Completed
let projectsCounter = document.getElementById('projectsCounter');
let projectsCount = 0;
let projectsTarget = 20;
let projectsInterval = setInterval(function() {
    projectsCount++;
    projectsCounter.textContent = projectsCount;
    
    if (projectsCount >= projectsTarget) {
        clearInterval(projectsInterval);
    }
}, 120); // Adjust the speed as needed

// Counter for Satisfied Clients
let clientsCounter = document.getElementById('clientsCounter');
let clientsCount = 0;
let clientsTarget = 100; // Representing 100%
let clientsInterval = setInterval(function() {
    clientsCount++;
    clientsCounter.textContent = clientsCount + '%';
    
    if (clientsCount >= clientsTarget) {
        clearInterval(clientsInterval);
    }
}, 25); // Adjust the speed as needed, different from the first counter for variety

document.addEventListener("DOMContentLoaded", function() {
    const items = document.querySelectorAll('.content-item');
    let activeIndex = 0; // Start with the first item

    function toggleContent() {
        // Remove 'active' class from all items
        items.forEach(item => item.classList.remove('active'));
        
        // Calculate the index of the next item
        activeIndex = (activeIndex + 1) % items.length;
        
        // Add 'active' class to the next item
        items[activeIndex].classList.add('active');
    }

    // Initial activation of the first content item
    toggleContent();

    // Set the interval to toggle content every 5 seconds
    setInterval(toggleContent, 8000);
});

document.addEventListener("DOMContentLoaded", function() {
    const pTags = document.querySelectorAll('#about p, #about-2 p'); // Assuming your p tags are within the #about section
    
    // Function to add the fade-in class to each p tag in sequence
    function animatePTagsSequentially() {
        pTags.forEach((p, index) => {
            // Delay each p tag's animation based on its order
            setTimeout(() => {
                p.classList.add('fade-in');
            }, index * 300); // Adjust time as needed. 300ms interval between each p tag's animation.
        });
    }

    animatePTagsSequentially();
});


document.addEventListener("DOMContentLoaded", function() {
    // Example: Switching to content-2 when something triggers this action
    switchContentTo('content-2');
});

function switchContentTo(contentId) {
    // Remove 'active' class from all content items
    document.querySelectorAll('.content-item').forEach(function(item) {
        item.classList.remove('active');
    });

    // Add 'active' class to the specified content item
    document.querySelector('.' + contentId).classList.add('active');
}
    



