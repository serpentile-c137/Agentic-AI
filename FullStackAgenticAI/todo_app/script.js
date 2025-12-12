document.addEventListener("DOMContentLoaded", () => {
    const todoInput = document.getElementById("todo-input");
    const addButton = document.getElementById("add-button");
    const todoList = document.getElementById("todo-list");

    // Function to add a new todo item
    const addTodo = () => {
        const todoText = todoInput.value.trim();

        if (todoText !== "") {
            const listItem = document.createElement("li");
            listItem.innerHTML = `
                <span>${todoText}</span>
                <div class="actions">
                    <button class="complete-btn">Complete</button>
                    <button class="delete-btn">Delete</button>
                </div>
            `;
            todoList.appendChild(listItem);
            todoInput.value = ""; // Clear the input field

            // Add event listeners for the new buttons
            listItem.querySelector(".complete-btn").addEventListener("click", () => {
                listItem.classList.toggle("completed");
            });

            listItem.querySelector(".delete-btn").addEventListener("click", () => {
                todoList.removeChild(listItem);
            });
        }
    };

    // Event listener for the Add button
    addButton.addEventListener("click", addTodo);

    // Event listener for pressing Enter key in the input field
    todoInput.addEventListener("keypress", (event) => {
        if (event.key === "Enter") {
            addTodo();
        }
    });
});
