document.addEventListener('DOMContentLoaded', () => {
  //reused variables
    const chatDisplay = document.getElementById('chat-display');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');

    // Function to display a message
    function displayMessage(content, isUser = false) {
      const message = document.createElement('div');
      message.textContent = content;
      message.className = isUser ? 'user-message' : 'bot-message';
      chatDisplay.appendChild(message);
      chatDisplay.scrollTop = chatDisplay.scrollHeight;
    }
  
    // Send message function
    sendButton.addEventListener('click', async () => {
      const query = userInput.value.trim();
      if (!query) return "No user input, please enter";
  
      // Display user message
      displayMessage(query, true);
  
      // Clear input field
      userInput.value = '';
      try {
        displayMessage("I'm thinking...")
        const response = await fetch('/search', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ user_input: query }),
        });
        if (response.ok) {
          const data = await response.json();
          console.log(data["topic"])
          chatbot_response = "The Bible states, \""+ data["verse"]
          chatDisplay.removeChild(chatDisplay.lastElementChild)
          displayMessage(chatbot_response);
        } else {
          displayMessage('I do not have an answer. Please enter a new question.');
        }
      } catch (error) {
        console.log("Error", error)
        displayMessage("An error has occured - contact developer or refresh page!");
      }
     });
  });
  