import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Task Manager",
    page_icon="✅",
    layout="centered"
)

# Initialize session state variables
if "tasks" not in st.session_state:
    st.session_state.tasks = []
if "task_status" not in st.session_state:
    st.session_state.task_status = []
if "filter_option" not in st.session_state:
    st.session_state.filter_option = "All"

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #4527A0;
        margin-bottom: 1rem;
    }
    .task-complete {
        text-decoration: line-through;
        color: #9E9E9E;
    }
    .task-container {
        background-color: #f8f9fa;
        border-radius: 5px;
        padding: 10px;
        margin: 10px 0;
    }
    .stButton button {
        width: 100%;
    }
    .task-count {
        color: #4527A0;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# App header
st.markdown('<p class="main-header">✅ Task Manager</p>', unsafe_allow_html=True)
st.markdown("*Organize your tasks efficiently*")

# Sidebar for app controls
with st.sidebar:
    st.header("Options")
    
    # Filter tasks
    st.subheader("Filter Tasks")
    filter_option = st.radio(
        "Show:",
        options=["All", "Active", "Completed"],
        index=0
    )
    st.session_state.filter_option = filter_option
    
    # Clear tasks
    if st.button("Clear Completed Tasks"):
        new_tasks = []
        new_status = []
        for task, status in zip(st.session_state.tasks, st.session_state.task_status):
            if not status:  # If not completed
                new_tasks.append(task)
                new_status.append(status)
        st.session_state.tasks = new_tasks
        st.session_state.task_status = new_status
        st.success("Completed tasks cleared!")
    
    # Reset all
    if st.button("Reset All Tasks"):
        st.session_state.tasks = []
        st.session_state.task_status = []
        st.success("All tasks reset!")

# Main content area
col1, col2 = st.columns([3, 1])

# Task input
with col1:
    new_task = st.text_input("Add a new task:", placeholder="Enter task description...")

with col2:
    st.write("")
    st.write("")
    if st.button("Add Task"):
        if new_task:
            # Add timestamp to make each task unique
            task_with_date = f"{new_task} ({datetime.now().strftime('%H:%M')})"
            st.session_state.tasks.append(task_with_date)
            st.session_state.task_status.append(False)
            st.success("Task added successfully!")
        else:
            st.warning("Please enter a task.")

# Display task count
total_tasks = len(st.session_state.tasks)
completed_tasks = sum(st.session_state.task_status)

if total_tasks > 0:
    st.markdown(f"<p class='task-count'>{completed_tasks}/{total_tasks} tasks completed</p>", unsafe_allow_html=True)

# Display tasks with checkboxes
if st.session_state.tasks:
    st.subheader("My Tasks")
    
    for i, (task, status) in enumerate(zip(st.session_state.tasks, st.session_state.task_status)):
        # Apply filter
        if (st.session_state.filter_option == "Active" and status) or \
           (st.session_state.filter_option == "Completed" and not status):
            continue
            
        col1, col2 = st.columns([4, 1])
        
        with col1:
            # Display task with or without strikethrough based on status
            if status:
                st.markdown(f"<div class='task-container'><span class='task-complete'>{task}</span></div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='task-container'>{task}</div>", unsafe_allow_html=True)
        
        with col2:
            # Toggle completion status
            if st.button("✓" if not status else "↺", key=f"toggle_{i}"):
                st.session_state.task_status[i] = not st.session_state.task_status[i]
                st.rerun()
            
            # Delete task
            if st.button("🗑️", key=f"delete_{i}"):
                st.session_state.tasks.pop(i)
                st.session_state.task_status.pop(i)
                st.success("Task removed!")
                st.rerun()
else:
    st.info("No tasks added yet. Add a task to get started!")

# Footer
st.markdown("---")
st.markdown("Built with Streamlit ❤️")
