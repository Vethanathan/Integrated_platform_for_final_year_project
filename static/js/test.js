const linkItems = document.querySelectorAll(".link-item");

linkItems.forEach((linkItem, index) => {
    linkItem.addEventListener("click", () => {
        document.querySelector(".active").classList.remove("active");
        linkItem.classList.add("active");

        const indicator = document.querySelector(".indicator");

        indicator.style.left = `${index * 95 + 48}px`;
    })
})

function delayRedirect(event, url) {
    event.preventDefault(); // prevent the default link behavior
    
    setTimeout(function() {
      window.location.href = url; // redirect after 2 seconds
    }, 2000); // delay for 2 seconds
  }
  function simulateKeyPress() {
    // Create a new keyboard event with the Ctrl+P key combination
    var event = new KeyboardEvent('keydown', {
      ctrlKey: true,
      keyCode: 80,
      charCode: 80
    });

    // Dispatch the keyboard event
    document.dispatchEvent(event);
  }