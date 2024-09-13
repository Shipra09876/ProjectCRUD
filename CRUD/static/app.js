URL2='http://127.0.0.1:8000/api/stuapi/'
const studentForm = document.getElementById('student-form');
const studentsList = document.getElementById('students-list');
const studentIdField = document.getElementById('student-id');

// Fetch all students on page load
document.addEventListener('DOMContentLoaded', getStudents);

// Handle form submission for creating and updating students
studentForm.addEventListener('submit', function(event) {
    event.preventDefault();
    const studentId = studentIdField.value;
    const studentData = {
        // id: studentIdField.value,
        name: document.getElementById('name').value,
        roll_no: document.getElementById('roll_no').value,
        city: document.getElementById('city').value
    };

    if (studentId) {
        updateStudent(studentId, studentData);
    } else {
        createStudent(studentData);
    }
});

// Fetch all students
function getStudents() {
    fetch(URL2, { method: 'GET' })
        .then(response => response.json())
        .then(data => renderStudents(data))
        .catch(error => console.error('Error:', error));
}

// Render students to the table
function renderStudents(students) {   
    studentsList.innerHTML = '';
    students.forEach(student => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${student.id}</td>
            <td>${student.name}</td>
            <td>${student.roll_no}</td>
            <td>${student.city}</td>
            <td>
                <button class="edit" onclick="editStudent(${student.id})">Edit</button>
                <button class="delete" onclick="deleteStudent(${student.id})">Delete</button>
            </td>
        `;
        studentsList.appendChild(row);
    });
}

// Create a new student
function createStudent(studentData) {
    fetch(URL2, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(studentData),
    })
    .then(response => response.json())
    .then(() => {
        studentForm.reset();
        getStudents();
    })
    .catch(error => console.error('Error:', error));
}

// Update an existing student
function updateStudent(studentId, studentData) {
    // studentData.id = studentId;
    fetch(URL2, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(studentData),
    })
    .then(response => response.json())
    .then(() => {
        studentForm.reset();
        studentIdField.value = '';
        getStudents();
    })
    .catch(error => console.error('Error:', error));
}

// Edit student (prefill the form)
function editStudent(studentId) {
    if (!studentId) {
        console.error('Student ID is undefined');
        return;
    }
    fetch(`${URL2}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(response => response.json())
    .then(data => {
        studentIdField.value = data.id;
        document.getElementById('name').value = data.name;
        document.getElementById('roll_no').value = data.roll_no;
        document.getElementById('city').value = data.city;
    })
    .catch(error => console.error('Error:', error));
}

// Delete student
function deleteStudent(studentId) {
    fetch(`${URL2}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ id: studentId }),
    })
    .then(response => response.json())
    .then(() => {
        getStudents();
    })
    .catch(error => console.error('Error:', error));
}


