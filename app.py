
import streamlit as st
import sqlite3
from datetime import date
from pathlib import Path

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="STACY | AI Academic Advisor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

DB_NAME = Path(__file__).parent / "stacy.db"

# ==========================================
# 2. DATABASE
# ==========================================

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS student_profile (
            id INTEGER PRIMARY KEY,
            name TEXT,
            college TEXT,
            degree TEXT,
            branch TEXT,
            semester TEXT,
            interests TEXT,
            goals TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS study_tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT,
            task TEXT,
            deadline TEXT,
            hours REAL,
            completed INTEGER DEFAULT 0
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS performance_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT,
            obtained REAL,
            total REAL,
            percentage REAL
        )
    """)

    conn.commit()
    conn.close()

init_db()

def get_profile():
    conn = get_connection()
    row = conn.execute(
        "SELECT * FROM student_profile WHERE id = 1"
    ).fetchone()
    conn.close()
    return row


# ==========================================
# 3. PREMIUM PURPLE-LAVENDER DESIGN
# ==========================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #f5f2fc;
    color: #30234f;
}

.block-container {
    max-width: 1300px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Headings */
h1, h2, h3 {
    color: #39256f !important;
    font-weight: 800 !important;
    letter-spacing: -0.5px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #241448, #49328b 60%, #7055bd);
}

section[data-testid="stSidebar"] * {
    color: #ffffff !important;
}

section[data-testid="stSidebar"] .stRadio label {
    background: rgba(255,255,255,0.08);
    padding: 11px 13px;
    border-radius: 12px;
    margin-bottom: 6px;
}

section[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(255,255,255,0.2);
}

/* Hero */
.hero {
    background: linear-gradient(120deg, #30205f, #6044a9, #9279db);
    border-radius: 23px;
    padding: 38px;
    color: white;
    margin: 10px 0 25px;
    box-shadow: 0 12px 30px rgba(65,43,126,0.17);
}

.hero h1, .hero h2, .hero p {
    color: white !important;
}

.hero h1 {
    font-size: 34px;
}

.hero p {
    color: #eee8ff !important;
}

.eyebrow {
    color: #d9ceff;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
    margin-bottom: 12px;
}

/* Feature cards */
.feature-card {
    background: #ffffff;
    border: 1px solid #e8e0f5;
    border-radius: 20px;
    padding: 24px;
    min-height: 155px;
    box-shadow: 0 6px 22px rgba(54,37,104,0.06);
    margin-bottom: 14px;
    transition: 0.2s ease;
}

.feature-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 26px rgba(54,37,104,0.12);
}

.feature-card h3 {
    font-size: 18px;
    margin: 10px 0 7px;
}

.feature-card p {
    color: #77718c;
    font-size: 13px;
}

.feature-icon {
    font-size: 27px;
}

/* Metrics */
div[data-testid="stMetric"] {
    background: white;
    border: 1px solid #e8e0f5;
    padding: 19px;
    border-radius: 17px;
    box-shadow: 0 5px 18px rgba(54,37,104,0.05);
}

div[data-testid="stMetricLabel"] {
    color: #77718c !important;
    font-weight: 600;
}

div[data-testid="stMetricValue"] {
    color: #49328b !important;
    font-weight: 800;
}

/* Buttons */
.stButton > button,
.stFormSubmitButton > button {
    background: linear-gradient(110deg, #49328b, #795ed0);
    color: #ffffff !important;
    border: none;
    border-radius: 12px;
    padding: 10px 20px;
    font-weight: 700;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background: #35216e;
    color: #ffffff !important;
    box-shadow: 0 5px 14px rgba(73,50,139,0.2);
}

/* Inputs */
.stTextInput input,
.stTextArea textarea,
.stNumberInput input,
[data-testid="stChatInput"] textarea {
    color: #30234f !important;
    background: #ffffff !important;
    border: 1px solid #ded4ef;
    border-radius: 11px;
}

.stTextInput input::placeholder,
.stTextArea textarea::placeholder,
[data-testid="stChatInput"] textarea::placeholder {
    color: #9389a8 !important;
    opacity: 1;
}

.stTextInput label,
.stNumberInput label,
.stTextArea label,
.stSelectbox label,
.stMultiSelect label {
    color: #49328b !important;
    font-weight: 700 !important;
}

/* Forms and containers */
div[data-testid="stForm"] {
    background: white;
    border: 1px solid #e8e0f5;
    border-radius: 18px;
    padding: 22px;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: white;
    border: 1px solid #e8e0f5;
    border-radius: 17px;
    padding: 12px;
}

/* AI chat */
div[data-testid="stChatMessage"] {
    background: white;
    border: 1px solid #e8e0f5;
    border-radius: 16px;
    padding: 14px;
    margin-bottom: 10px;
}

[data-testid="stChatMessage"] table {
    border-collapse: collapse;
}

[data-testid="stChatMessage"] table th,
[data-testid="stChatMessage"] table td {
    color: #30234f !important;
    background: #f3efff !important;
    border: 1px solid #cfc2e8 !important;
    padding: 10px !important;
}

[data-testid="stChatMessage"] table th {
    background: #e4d9ff !important;
    font-weight: 700 !important;
}

/* Progress bar */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #6549b3, #a18be9);
}

/* General text */
.stApp p {
    color: #51456f;
}

hr {
    border-color: #e9e3f4;
}

.task-card {
    background: white;
    border: 1px solid #ebe6f6;
    border-radius: 15px;
    padding: 17px 20px;
    margin: 8px 0;
}

.task-card strong {
    color: #39256f;
}

.small-muted {
    color: #827b98;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# 4. GROQ CONNECTION

def get_groq_client():
    try:
        from groq import Groq

        api_key = st.secrets.get("GROQ_API_KEY", "")

        if not api_key:
            return None

        return Groq(api_key=api_key)

    except Exception:
        return None

def ask_ai(prompt, system_message):
    client = get_groq_client()

    if client is None:
        return (
            "I couldn't connect to the AI service. "
            "Please check that Groq is installed and your "
            "GROQ_API_KEY is correctly configured in secrets.toml."
        )

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1500
    )

    return response.choices[0].message.content

# ==========================================
# 5. SIDEBAR NAVIGATION
# ==========================================

with st.sidebar:
    st.markdown("""
    <div style="padding:12px 5px 22px 5px;">
        <div style="font-size:35px;">🎓</div>
        <div style="font-size:27px;font-weight:800;letter-spacing:1px;">
            STACY
        </div>
        <div style="font-size:12px;color:#e4dcff;">
            YOUR AI ACADEMIC COMPANION
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("**NAVIGATION**")

    page = st.radio(
        "Navigate",
        [
            "🏠 Dashboard",
            "👤 Student Profile",
            "🤖 AI Academic Advisor",
            "📚 Study Planner",
            "📊 My Performance",
            "🚀 Career Guidance"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")
    profile = get_profile()

    if profile and profile[1]:
        st.markdown(f"**Welcome, {profile[1]}!**")
    else:
        st.markdown("**Welcome, Student!**")

    st.caption("Learn smarter. Plan better. Grow further.")

# ==========================================
# 6. DASHBOARD
# ==========================================

if page == "🏠 Dashboard":

    profile = get_profile()
    student_name = profile[1] if profile and profile[1] else "Student"

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM study_tasks")
    total_tasks = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM study_tasks WHERE completed = 1"
    )
    completed_tasks = cursor.fetchone()[0]



    cursor.execute("SELECT AVG(percentage) FROM performance_records")
    average = cursor.fetchone()[0]

    conn.close()

    st.markdown(f"""
    <div class="hero">
        <div class="eyebrow">YOUR PERSONAL ACADEMIC SPACE</div>
        <h1>Welcome back, {student_name} 👋</h1>
        <p>Your journey to academic success starts with one smart step.
        Let's make today productive!</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Your Academic Overview")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("📚 Total Study Tasks", total_tasks)

    with c2:
        st.metric("✅ Tasks Completed", completed_tasks)

    with c3:
        st.metric(
            "📈 Average Performance",
            f"{average:.1f}%" if average is not None else "Not available"
        )

    st.markdown("---")
    st.subheader("Explore STACY")

    cards = [
        ("👤", "Student Profile", "Keep your academic information and goals organised."),
        ("🤖", "AI Academic Advisor", "Get instant help with concepts, doubts and learning."),
        ("📚", "Study Planner", "Organise assignments, subjects and study deadlines."),
        ("📊", "My Performance", "Track your marks and monitor your progress."),
        ("🚀", "Career Guidance", "Discover career paths based on your interests and skills."),
        ("✨", "Your Growth", "Build better study habits and work towards your goals.")
    ]

    for start in range(0, len(cards), 3):
        cols = st.columns(3)

        for col, item in zip(cols, cards[start:start + 3]):
            with col:
                st.markdown(f"""
                <div class="feature-card">
                    <div class="feature-icon">{item[0]}</div>
                    <h3>{item[1]}</h3>
                    <p>{item[2]}</p>
                </div>
                """, unsafe_allow_html=True)

    st.caption("STACY — Your personal AI Academic Advisor")

# ==========================================
# 7. STUDENT PROFILE
# ==========================================

elif page == "👤 Student Profile":

    st.title("👤 Student Profile")
    st.write("Tell STACY about yourself so it can better support your academic journey.")

    profile = get_profile()

    with st.form("profile_form"):

        name = st.text_input(
            "Full Name",
            value=profile[1] if profile else ""
        )

        college = st.text_input(
            "College / University",
            value=profile[2] if profile else ""
        )

        degree = st.text_input(
            "Degree",
            value=profile[3] if profile else "B.Tech"
        )

        branch = st.text_input(
            "Branch / Specialisation",
            value=profile[4] if profile else ""
        )

        semester = st.selectbox(
            "Current Semester",
            ["1st Semester", "2nd Semester", "3rd Semester",
             "4th Semester", "5th Semester", "6th Semester",
             "7th Semester", "8th Semester"],
            index=(
                ["1st Semester", "2nd Semester", "3rd Semester",
                 "4th Semester", "5th Semester", "6th Semester",
                 "7th Semester", "8th Semester"].index(profile[5])
                if profile and profile[5] in
                ["1st Semester", "2nd Semester", "3rd Semester",
                 "4th Semester", "5th Semester", "6th Semester",
                 "7th Semester", "8th Semester"] else 0
            )
        )

        interests = st.text_area(
            "Academic Interests",
            value=profile[6] if profile else "",
            placeholder="For example: Python, AI, Web Development..."
        )

        goals = st.text_area(
            "Academic and Career Goals",
            value=profile[7] if profile else "",
            placeholder="What do you want to achieve?"
        )

        submitted = st.form_submit_button(
            "💾 Save My Profile",
            use_container_width=True
        )

        if submitted:
            if not name.strip():
                st.error("Please enter your name.")
            else:
                conn = get_connection()
                conn.execute("""
                    INSERT OR REPLACE INTO student_profile
                    (id, name, college, degree, branch, semester, interests, goals)
                    VALUES (1, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    name, college, degree, branch,
                    semester, interests, goals
                ))
                conn.commit()
                conn.close()

                st.success("Your student profile has been saved!")
                st.rerun()

# ==========================================
# 8. AI ACADEMIC ADVISOR
# ==========================================

elif page == "🤖 AI Academic Advisor":

    st.title("🤖 AI Academic Advisor")
    st.write("Ask questions, understand difficult concepts and learn at your own pace.")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask STACY anything about your studies...")

    if prompt:
        st.session_state.chat_history.append({
            "role": "user",
            "content": prompt
        })

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("STACY is thinking..."):
                try:
                    answer = ask_ai(
                        prompt,
                        "You are STACY, a friendly and knowledgeable AI "
                        "academic advisor for college students. Explain "
                        "concepts simply, step by step, using examples. "
                        "Encourage students to understand rather than memorise."
                    )
                except Exception as error:
                    answer = f"Sorry, something went wrong: {error}"

                st.markdown(answer)

        st.session_state.chat_history.append({
            "role": "assistant",
            "content": answer
        })

    if st.session_state.chat_history:
        if st.button("🗑️ Clear Chat"):
            st.session_state.chat_history = []
            st.rerun()

# ==========================================

# ==========================================
# 9. STUDY PLANNER
# ==========================================

elif page == "📚 Study Planner":

    st.title("📚 Study Planner")
    st.write("Plan your study sessions and stay on top of your tasks.")

    # --------------------------------------
    # ADD NEW STUDY TASK
    # --------------------------------------

    with st.expander("➕ Add a New Study Task", expanded=True):

        with st.form("task_form"):

            subject = st.text_input("Subject")
            task = st.text_input("Task / Assignment")

            deadline = st.date_input(
                "Deadline",
                min_value=date.today()
            )

            hours = st.number_input(
                "Estimated Study Hours",
                min_value=0.5,
                max_value=100.0,
                value=1.0,
                step=0.5
            )

            submitted = st.form_submit_button(
                "➕ Add Task",
                use_container_width=True
            )

            if submitted:

                if not subject.strip() or not task.strip():
                    st.error("Please enter both subject and task.")

                else:
                    conn = get_connection()

                    conn.execute("""
                        INSERT INTO study_tasks
                        (subject, task, deadline, hours, completed)
                        VALUES (?, ?, ?, ?, 0)
                    """, (
                        subject.strip(),
                        task.strip(),
                        str(deadline),
                        hours
                    ))

                    conn.commit()
                    conn.close()

                    st.success("Your task has been added!")
                    st.rerun()

    # --------------------------------------
    # FETCH STUDY TASKS
    # --------------------------------------

    conn = get_connection()

    tasks = conn.execute("""
        SELECT id, subject, task, deadline, hours, completed
        FROM study_tasks
        ORDER BY deadline ASC
    """).fetchall()

    conn.close()

    today = date.today()

    completed_tasks = [
        item for item in tasks if item[5] == 1
    ]

    pending_tasks = [
        item for item in tasks if item[5] == 0
    ]

    overdue_tasks = [
        item for item in pending_tasks
        if date.fromisoformat(item[3]) < today
    ]

    total_hours = sum(item[4] for item in tasks)

    completed_hours = sum(
        item[4] for item in completed_tasks
    )

    progress = (
        len(completed_tasks) / len(tasks)
        if tasks else 0
    )

    # --------------------------------------
    # STUDY STATISTICS
    # --------------------------------------

    st.markdown("---")
    st.subheader("📊 Study Statistics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Tasks",
        len(tasks)
    )

    col2.metric(
        "Completed",
        len(completed_tasks)
    )

    col3.metric(
        "Pending",
        len(pending_tasks)
    )

    col4.metric(
        "Overdue",
        len(overdue_tasks)
    )

    st.markdown("### ⏱️ Study Hours")

    col1, col2 = st.columns(2)

    col1.metric(
        "Total Planned Hours",
        f"{total_hours:.1f} hrs"
    )

    col2.metric(
        "Completed Study Hours",
        f"{completed_hours:.1f} hrs"
    )

    st.markdown("### 🎯 Overall Progress")

    st.progress(progress)

    st.caption(
        f"{len(completed_tasks)} of {len(tasks)} tasks completed "
        f"({progress * 100:.0f}%)"
    )

    # --------------------------------------
    # OVERDUE TASK ALERTS
    # --------------------------------------

    if overdue_tasks:

        st.markdown("---")
        st.subheader("⚠️ Overdue Tasks")

        for item in overdue_tasks:

            task_id, subject, task_name, deadline, hours, completed = item

            with st.container(border=True):

                st.error(
                    f"⚠️ {task_name} — {subject}"
                )

                st.caption(
                    f"Deadline: {deadline} · "
                    f"{hours:.1f} study hours"
                )

    # --------------------------------------
    # PENDING STUDY TASKS
    # --------------------------------------

    st.markdown("---")
    st.subheader("📚 Your Study Tasks")

    if not tasks:

        st.info("No study tasks yet. Add your first task above!")

    else:

        for item in tasks:

            task_id, subject, task_name, deadline, hours, completed = item

            task_date = date.fromisoformat(deadline)

            with st.container(border=True):

                col1, col2 = st.columns([5, 1])

                with col1:

                    if completed:

                        st.markdown(f"~~**{task_name}**~~")
                        st.caption(
                            f"✅ {subject} · Completed"
                        )

                    else:

                        st.markdown(f"**{task_name}**")

                        if task_date < today:
                            st.error(
                                f"Overdue · {subject} · {deadline}"
                            )

                        elif task_date == today:
                            st.warning(
                                f"Due today · {subject} · {deadline}"
                            )

                        else:
                            st.caption(
                                f"📘 {subject} · 📅 {deadline}"
                            )

                        st.caption(
                            f"⏱️ Estimated time: {hours:.1f} hours"
                        )

                with col2:

                    new_status = st.checkbox(
                        "Done",
                        value=bool(completed),
                        key=f"task_{task_id}"
                    )

                    if new_status != bool(completed):

                        conn = get_connection()

                        conn.execute("""
                            UPDATE study_tasks
                            SET completed = ?
                            WHERE id = ?
                        """, (
                            int(new_status),
                            task_id
                        ))

                        conn.commit()
                        conn.close()

                        st.rerun()

                # --------------------------------------
                # EDIT TASK
                # --------------------------------------

                with st.expander("✏️ Edit Task"):

                    with st.form(f"edit_task_{task_id}"):

                        edited_subject = st.text_input(
                            "Subject",
                            value=subject
                        )

                        edited_task = st.text_input(
                            "Task / Assignment",
                            value=task_name
                        )

                        edited_deadline = st.date_input(
                            "Deadline",
                            value=task_date,
                            key=f"deadline_{task_id}"
                        )

                        edited_hours = st.number_input(
                            "Estimated Study Hours",
                            min_value=0.5,
                            max_value=100.0,
                            value=float(hours),
                            step=0.5,
                            key=f"hours_{task_id}"
                        )

                        update_task = st.form_submit_button(
                            "💾 Save Changes",
                            use_container_width=True
                        )

                        if update_task:

                            if not edited_subject.strip() or not edited_task.strip():

                                st.error(
                                    "Subject and task cannot be empty."
                                )

                            else:

                                conn = get_connection()

                                conn.execute("""
                                    UPDATE study_tasks
                                    SET subject = ?,
                                        task = ?,
                                        deadline = ?,
                                        hours = ?
                                    WHERE id = ?
                                """, (
                                    edited_subject.strip(),
                                    edited_task.strip(),
                                    str(edited_deadline),
                                    edited_hours,
                                    task_id
                                ))

                                conn.commit()
                                conn.close()

                                st.success("Task updated successfully!")
                                st.rerun()

                # --------------------------------------
                # DELETE TASK
                # --------------------------------------

                if st.button(
                    "🗑️ Delete Task",
                    key=f"delete_{task_id}"
                ):

                    conn = get_connection()

                    conn.execute(
                        "DELETE FROM study_tasks WHERE id = ?",
                        (task_id,)
                    )

                    conn.commit()
                    conn.close()

                    st.success("Task deleted successfully!")
                    st.rerun()

# 10. MY PERFORMANCE TRACKER
# ==========================================

elif page == "📊 My Performance":

    st.title("📊 My Performance Tracker")
    st.write("Add, edit and manage your academic results.")

    # --------------------------------------
    # ADD OR UPDATE SUBJECT
    # --------------------------------------

    with st.container(border=True):

        st.subheader("➕ Add or Update Subject")
        st.caption(
            "Enter an existing subject name to update its marks. "
            "Enter a new name to add a new subject."
        )

        with st.form("performance_form"):

            subject = st.text_input("Subject Name")

            col1, col2 = st.columns(2)

            with col1:
                obtained = st.number_input(
                    "Marks Obtained",
                    min_value=0.0,
                    value=0.0,
                    step=1.0
                )

            with col2:
                total = st.number_input(
                    "Total Marks",
                    min_value=1.0,
                    value=100.0,
                    step=1.0
                )

            submitted = st.form_submit_button(
                "💾 Save / Update Subject",
                use_container_width=True
            )

            if submitted:

                if not subject.strip():
                    st.error("Please enter a subject name.")

                elif obtained > total:
                    st.error(
                        "Obtained marks cannot exceed total marks."
                    )

                else:
                    conn = get_connection()

                    # Find existing subject, ignoring case and extra spaces
                    existing = conn.execute("""
                        SELECT id
                        FROM performance_records
                        WHERE LOWER(TRIM(subject)) = LOWER(TRIM(?))
                        ORDER BY id ASC
                    """, (subject.strip(),)).fetchall()

                    percentage = (obtained / total) * 100

                    if existing:

                        # Update the first matching record
                        main_id = existing[0][0]

                        conn.execute("""
                            UPDATE performance_records
                            SET subject = ?,
                                obtained = ?,
                                total = ?,
                                percentage = ?
                            WHERE id = ?
                        """, (
                            subject.strip(),
                            obtained,
                            total,
                            percentage,
                            main_id
                        ))

                        # Remove any older duplicate records
                        for duplicate in existing[1:]:
                            conn.execute(
                                "DELETE FROM performance_records WHERE id = ?",
                                (duplicate[0],)
                            )

                        message = f"{subject} updated successfully!"

                    else:

                        # Add a new subject
                        conn.execute("""
                            INSERT INTO performance_records
                            (subject, obtained, total, percentage)
                            VALUES (?, ?, ?, ?)
                        """, (
                            subject.strip(),
                            obtained,
                            total,
                            percentage
                        ))

                        message = f"{subject} added successfully!"

                    conn.commit()
                    conn.close()

                    st.success(message)
                    st.rerun()

    # --------------------------------------
    # EDIT EXISTING SUBJECT
    # --------------------------------------

    st.markdown("---")
    st.subheader("✏️ Edit Existing Subject")

    conn = get_connection()

    records = conn.execute("""
        SELECT id, subject, obtained, total, percentage
        FROM performance_records
        ORDER BY subject ASC, id ASC
    """).fetchall()

    conn.close()

    if records:

        selected_id = st.selectbox(
            "Select a subject to edit",
            options=[record[0] for record in records],
            format_func=lambda selected_id: next(
                f"{record[1]} ({record[4]:.1f}%)"
                for record in records
                if record[0] == selected_id
            ),
            key="edit_subject_selection"
        )

        selected_record = next(
            record for record in records
            if record[0] == selected_id
        )

        with st.form("edit_performance_form"):

            st.write(f"Editing: **{selected_record[1]}**")

            edited_subject = st.text_input(
                "Subject Name",
                value=selected_record[1]
            )

            col1, col2 = st.columns(2)

            with col1:
                edited_obtained = st.number_input(
                    "Marks Obtained",
                    min_value=0.0,
                    value=float(selected_record[2]),
                    step=1.0,
                    key="edit_obtained"
                )

            with col2:
                edited_total = st.number_input(
                    "Total Marks",
                    min_value=1.0,
                    value=float(selected_record[3]),
                    step=1.0,
                    key="edit_total"
                )

            update_button = st.form_submit_button(
                "✏️ Update Selected Subject",
                use_container_width=True
            )

            if update_button:

                if not edited_subject.strip():
                    st.error("Subject name cannot be empty.")

                elif edited_obtained > edited_total:
                    st.error(
                        "Obtained marks cannot exceed total marks."
                    )

                else:
                    conn = get_connection()

                    # Check whether the renamed subject already exists
                    conflicts = conn.execute("""
                        SELECT id
                        FROM performance_records
                        WHERE LOWER(TRIM(subject)) = LOWER(TRIM(?))
                        AND id != ?
                    """, (
                        edited_subject.strip(),
                        selected_id
                    )).fetchall()

                    if conflicts:
                        st.error(
                            "Another record already uses this subject name. "
                            "Use Add or Update Subject above to update it."
                        )

                    else:
                        percentage = (
                            edited_obtained / edited_total
                        ) * 100

                        conn.execute("""
                            UPDATE performance_records
                            SET subject = ?,
                                obtained = ?,
                                total = ?,
                                percentage = ?
                            WHERE id = ?
                        """, (
                            edited_subject.strip(),
                            edited_obtained,
                            edited_total,
                            percentage,
                            selected_id
                        ))

                        conn.commit()
                        st.success("Subject updated successfully!")

                    conn.close()

                    if not conflicts:
                        st.rerun()

    else:
        st.info("Add your first subject to start tracking performance.")

    # --------------------------------------
    # DELETE SUBJECT
    # --------------------------------------

    if records:

        st.markdown("---")
        st.subheader("🗑️ Delete a Subject")

        delete_id = st.selectbox(
            "Choose a subject to delete",
            options=[record[0] for record in records],
            format_func=lambda selected_id: next(
                record[1]
                for record in records
                if record[0] == selected_id
            ),
            key="delete_subject_selection"
        )

        if st.button("🗑️ Delete Selected Subject"):

            conn = get_connection()
            conn.execute(
                "DELETE FROM performance_records WHERE id = ?",
                (delete_id,)
            )
            conn.commit()
            conn.close()

            st.success("Subject deleted successfully!")
            st.rerun()

    # --------------------------------------
    # ACADEMIC RESULTS
    # --------------------------------------

    st.markdown("---")
    st.subheader("📈 Your Academic Results")

    conn = get_connection()

    records = conn.execute("""
        SELECT id, subject, obtained, total, percentage
        FROM performance_records
        ORDER BY subject ASC
    """).fetchall()

    conn.close()

    if records:

        total_obtained = sum(record[2] for record in records)
        total_marks = sum(record[3] for record in records)

        overall_average = (
            total_obtained / total_marks * 100
            if total_marks else 0
        )

        col1, col2, col3 = st.columns(3)

        col1.metric("Subjects Recorded", len(records))

        col2.metric(
            "Total Marks",
            f"{total_obtained:g}/{total_marks:g}"
        )

        col3.metric(
            "Overall Percentage",
            f"{overall_average:.2f}%"
        )

        st.markdown("### Subject-wise Performance")

        for record in records:

            record_id, subject, obtained, total, percentage = record

            with st.container(border=True):

                st.markdown(f"**📘 {subject}**")

                st.progress(min(percentage / 100, 1.0))

                st.caption(
                    f"{obtained:g} / {total:g} marks · "
                    f"{percentage:.2f}%"
                )

    else:
        st.info("No performance records available yet.")

# ==========================================
# 11. CAREER GUIDANCE
# ==========================================

elif page == "🚀 Career Guidance":

    st.markdown("""
        <div class="section-header">
            <h1>🚀 Career Guidance</h1>
            <p>Discover career possibilities based on your interests,
            skills, strengths and future goals.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🎓 Tell us about yourself")

    with st.form("career_form"):

        col1, col2 = st.columns(2)

        with col1:
            student_name = st.text_input(
                "Student Name",
                placeholder="Enter your name"
            )

            education = st.selectbox(
                "Current Education Level",
                [
                    "Class 9",
                    "Class 10",
                    "Class 11",
                    "Class 12",
                    "Undergraduate",
                    "Postgraduate"
                ]
            )

            stream = st.selectbox(
                "Your Stream",
                [
                    "Science (PCM)",
                    "Science (PCB)",
                    "Commerce",
                    "Arts / Humanities",
                    "Computer Science",
                    "Other"
                ]
            )

        with col2:
            favourite_subject = st.selectbox(
                "Favourite Subject",
                [
                    "Mathematics",
                    "Science",
                    "Computer Science",
                    "English",
                    "Economics",
                    "Business Studies",
                    "History",
                    "Political Science",
                    "Biology",
                    "Other"
                ]
            )

            career_goal = st.selectbox(
                "Preferred Career Field",
                [
                    "Technology & IT",
                    "Engineering",
                    "Medical & Healthcare",
                    "Business & Management",
                    "Finance & Banking",
                    "Law",
                    "Government Services",
                    "Design & Creativity",
                    "Teaching & Education",
                    "Research",
                    "Not Sure Yet"
                ]
            )

            study_preference = st.selectbox(
                "Preferred Work Style",
                [
                    "Working with people",
                    "Working with technology",
                    "Creative work",
                    "Research and analysis",
                    "Business and leadership",
                    "Helping others",
                    "Not Sure"
                ]
            )

        st.markdown("---")
        st.markdown("### 💡 Your Interests")

        interests = st.multiselect(
            "Select your interests",
            [
                "Technology",
                "Artificial Intelligence",
                "Coding",
                "Robotics",
                "Science",
                "Medicine",
                "Business",
                "Entrepreneurship",
                "Finance",
                "Art and Design",
                "Writing",
                "Sports",
                "Psychology",
                "Teaching",
                "Law",
                "Public Speaking"
            ]
        )

        st.markdown("### 🧠 Your Skills")

        skills = st.multiselect(
            "Select your strongest skills",
            [
                "Problem Solving",
                "Communication",
                "Leadership",
                "Creativity",
                "Analytical Thinking",
                "Mathematics",
                "Programming",
                "Teamwork",
                "Decision Making",
                "Critical Thinking",
                "Research",
                "Time Management"
            ]
        )

        st.markdown("### ⭐ Additional Information")

        strengths = st.text_area(
            "What are your biggest strengths?",
            placeholder="Describe your strengths..."
        )

        future_goals = st.text_area(
            "What do you want to achieve in the future?",
            placeholder="Describe your dreams and ambitions..."
        )

        submitted = st.form_submit_button(
            "🚀 Discover My Career Path",
            use_container_width=True
        )

    if submitted:

        if not student_name.strip():
            st.warning("Please enter your name.")

        elif not interests:
            st.warning("Please select at least one interest.")

        elif not skills:
            st.warning("Please select at least one skill.")

        else:

            st.session_state["career_profile"] = {
                "name": student_name,
                "education": education,
                "stream": stream,
                "favourite_subject": favourite_subject,
                "career_goal": career_goal,
                "study_preference": study_preference,
                "interests": interests,
                "skills": skills,
                "strengths": strengths,
                "future_goals": future_goals
            }

            st.success("Your career profile has been created!")

            st.markdown("---")
            st.markdown("## 🎯 Your Career Profile")

            st.write(f"**Student:** {student_name}")
            st.write(f"**Education:** {education}")
            st.write(f"**Stream:** {stream}")
            st.write(f"**Favourite Subject:** {favourite_subject}")
            st.write(f"**Preferred Career:** {career_goal}")

            st.markdown("### 💡 Your Interests")
            st.write(", ".join(interests))

            st.markdown("### 🧠 Your Skills")
            st.write(", ".join(skills))

            st.markdown("### 🌟 Career Suggestions")

            career_suggestions = {
                "Technology & IT": [
                    "Software Developer",
                    "AI / Machine Learning Engineer",
                    "Data Scientist",
                    "Cybersecurity Analyst"
                ],
                "Engineering": [
                    "Mechanical Engineer",
                    "Civil Engineer",
                    "Electrical Engineer",
                    "Computer Engineer"
                ],
                "Medical & Healthcare": [
                    "Doctor",
                    "Pharmacist",
                    "Biotechnologist",
                    "Healthcare Researcher"
                ],
                "Business & Management": [
                    "Business Analyst",
                    "Entrepreneur",
                    "Marketing Manager",
                    "Management Consultant"
                ],
                "Finance & Banking": [
                    "Financial Analyst",
                    "Chartered Accountant",
                    "Investment Analyst",
                    "Economist"
                ],
                "Law": [
                    "Lawyer",
                    "Legal Advisor",
                    "Corporate Lawyer",
                    "Judicial Services"
                ],
                "Government Services": [
                    "Civil Services Officer",
                    "Government Administrator",
                    "Defence Services",
                    "Public Policy Analyst"
                ],
                "Design & Creativity": [
                    "Graphic Designer",
                    "UI/UX Designer",
                    "Animator",
                    "Creative Director"
                ],
                "Teaching & Education": [
                    "Teacher",
                    "Professor",
                    "Education Consultant",
                    "Instructional Designer"
                ],
                "Research": [
                    "Research Scientist",
                    "Data Researcher",
                    "Academic Researcher",
                    "Laboratory Scientist"
                ]
            }

            suggestions = career_suggestions.get(
                career_goal,
                [
                    "Software Developer",
                    "Business Analyst",
                    "Researcher",
                    "Entrepreneur"
                ]
            )

            for i, career in enumerate(suggestions, 1):
                st.markdown(f"**{i}. {career}**")

            st.info(
                "These are preliminary career suggestions based on "
                "your preferred career field. A deeper assessment of "
                "your interests, skills and aptitude is needed to "
                "identify the best career match."
            )

# ==========================================
# 12. FOOTER
# ==========================================

st.markdown("---")
st.markdown(
    "<div style='text-align:center;color:#928ba7;font-size:12px;'>"
    "STACY · AI Academic Advisor · Learn smarter, grow further."
    "</div>",
    unsafe_allow_html=True
)
