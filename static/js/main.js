document.addEventListener("DOMContentLoaded", function () {
    console.log("Website loaded!");


    // Toggle Mobile Navigation Menu
    
    const menuToggle = document.getElementById("menu-toggle");
    const navMenu = document.getElementById("nav-menu");

    if (menuToggle && navMenu) {
        menuToggle.addEventListener("click", function () {
            navMenu.classList.toggle("open");
        });
    }

    
    //  Smooth Scrolling for Navigation Links
  
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener("click", function (e) {
            e.preventDefault();
            const targetId = this.getAttribute("href").substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 50,
                    behavior: "smooth"
                });
            }
        });
    });

    
    //  Chatbot Functionality (AJAX + Django)
    
    const chatInput = document.getElementById("chat-input");
    const chatSendBtn = document.getElementById("chat-send");
    const chatBox = document.getElementById("chat-box");

    if (chatSendBtn && chatInput && chatBox) {
        chatSendBtn.addEventListener("click", sendMessage);
        chatInput.addEventListener("keypress", function (e) {
            if (e.key === "Enter") sendMessage();
        });

        function sendMessage() {
            const userInput = chatInput.value;
            
            if (userInput.trim() === "") return; // Prevent empty messages
            
            // Append User Message
            chatBox.innerHTML += `
                <div class="message user">
                    <strong>You:</strong> ${userInput}
                </div>
            `;

            // Send Data To Django Backend
            fetch("/chatbot/", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken()
                },
                body: JSON.stringify({ message: userInput })
            })
            .then(response => response.json())
            .then(data => {
                // Append Chatbot Response
                chatBox.innerHTML += `
                    <div class="message bot">
                        <strong>Bot:</strong> ${data.response}
                    </div>
                `;
                chatInput.value = "";
                chatBox.scrollTop = chatBox.scrollHeight;
            })
            .catch(error => console.error('Error:', error));
        }

        // Function To Get CSRF Token (Important for Django)
        function getCSRFToken() {
            return document.querySelector('[name=csrfmiddlewaretoken]').value;
        }
    }

    
    //  Event Concept Generator Functionality
    
    const generateIdeaBtn = document.getElementById("generate-idea-btn");
    const eventIdeaContainer = document.getElementById("event-idea");

    if (generateIdeaBtn && eventIdeaContainer) {
        generateIdeaBtn.addEventListener("click", function () {
            eventIdeaContainer.innerText = "Generating Idea... Please wait.";

            // Send Request To Django Backend
            fetch("/ai_generate/", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken()
                },
                body: JSON.stringify({})
            })
            .then(response => response.json())
            .then(data => {
                eventIdeaContainer.innerText = data.idea;
            })
            .catch(error => {
                eventIdeaContainer.innerText = "Failed to generate idea. Try again.";
                console.error('Error:', error);
            });
        });
    }

    
    // Handle CSRF Token for Django
    
    function getCSRFToken() {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith('csrftoken=')) {
                    cookieValue = decodeURIComponent(cookie.substring(10));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
