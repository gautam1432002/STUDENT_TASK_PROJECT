# Student Task Manager (Futuristic SPA)

**Developer:** Gautam Verma (B.Tech CSE, SVCE Indore)

**Project Title & Goal:** A Single Page Application (SPA) built with Django and Vanilla JavaScript that allows students to track and manage homework tasks with a modern Glassmorphism UI, featuring asynchronous additions and deletions without page reloads.

## 1. Setup Instructions
To run this project locally:

1. **Clone the repository:**
    ```bash
    git clone <YOUR_GITHUB_REPO_LINK_HERE>
    cd student_task_manager
    ```

2. **Install dependencies:**
    ```bash
    pip install django
    ```

3. **Run Migrations:**
    ```bash
    python manage.py migrate
    ```

4. **Start the Server:**
    ```bash
    python manage.py runserver
    ```
    Access the app at `http://127.0.0.1:8000/`.

## 2. The Logic (How I thought)

### Why did you choose this approach?
* **Backend:** I chose **Django** because of its robust ORM and rapid setup capabilities. Using `JsonResponse`, I created a lightweight API to serve the frontend.
* **Frontend:** I opted for **Vanilla JavaScript** combined with **Tailwind CSS**. I avoided heavy frameworks (like React) to keep the project lightweight and to demonstrate core understanding of DOM manipulation and the Fetch API.
* **UI/UX:** I implemented a "Glassmorphism" design aesthetic to give the application a modern, futuristic feel, utilizing CSS backdrop-filters and smooth CSS animations for a better user experience.

### What was the hardest bug you faced, and how did you fix it?
* **Challenge:** I faced a challenge syncing the "Delete" functionality with the UI. Initially, when using standard browser alerts (`confirm()`), the UI felt disconnected. Switching to a custom Modal created issues where the code execution didn't "pause" like a standard alert, causing the delete function to trigger immediately or not at all.
* **Fix:** I refactored the JavaScript logic to separate the "Modal Open" event from the "Confirm Delete" action. I used a global variable to temporarily store the `taskId` when the modal opens, and only triggered the `fetch()` DELETE request when the user explicitly clicked "Yes" inside the custom modal.

## 3. Output Screenshots

![Task Manager UI](screenshots/preview-1.png) & (screenshots/preview-2.png) 
*(Screenshot showing the Task List, Glassmorphism UI, and Custom Toast Notifications)*

## 4. Future Improvements
If I had 2 more days, I would add:
1. **User Authentication:** Implement Django User Auth so students can log in and see only their specific private tasks.
2. **Due Dates & Sorting:** Add a DateTime field to tasks and allow sorting by "Due Soonest".
3. **Drag & Drop:** Implement a drag-and-drop interface to reorder tasks based on priority.

---

