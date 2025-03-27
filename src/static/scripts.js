/*import {classes} from './schedule_complete.js';

const submitBtn = document.querySelector('#submit');
submitBtn.addEventListener("click", () => {
    let classOne = document.querySelector('input[name="class1"]');
    localStorage.setItem('first-class', classOne.value);
    let classTwo = document.querySelector('input[name="class2"]');
    localStorage.setItem('second-class', classTwo.value);
    let classThree = document.querySelector('input[name="class3"]');
    localStorage.setItem('third-class', classThree.value);
    let classFour = document.querySelector('input[name="class4"]');
    localStorage.setItem('fourth-class', classFour.value);
    let classFive = document.querySelector('input[name="class5"]');
    localStorage.setItem('fifth-class', classFive.value);
    let classSix = document.querySelector('input[name="class6"]');
    localStorage.setItem('sixth-class', classSix.value);
    let classSeven = document.querySelector('input[name="class7"]');
    localStorage.setItem('seventh-class', classSeven.value);
    let classEight = document.querySelector('input[name="class8"]');
    localStorage.setItem('eighth-class', classEight.value);
    let classNine = document.querySelector('input[name="class9"]');
    localStorage.setItem('ninth-class', classNine.value);
    let classTen = document.querySelector('input[name="class10"]');
    localStorage.setItem('tenth-class', classTen.value);
})

const resetBtn = document.querySelector("#reset");
resetBtn.addEventListener('click', () => {
    localStorage.removeItem('class1');
    localStorage.removeItem('class2');
    localStorage.removeItem('class3');
    localStorage.removeItem('class4');
    localStorage.removeItem('class5');
    localStorage.removeItem('class6');
    localStorage.removeItem('class7');
    localStorage.removeItem('class8');
    localStorage.removeItem('class9');
    localStorage.removeItem('class10');
    location.reload();
})

const check = localStorage.getItem('class1');
if (check === null) {
    document.querySelector('#form').className = 'show';
    document.querySelector('#class_information').className = 'hide';
} else {
    document.querySelector('#form').className = 'hide';
    document.querySelector('#class_information').className = 'show'
    const classInfo = document.querySelector('#class_information');

    for (let x = 0; x < classes.length; x++) {
        let information = document.createElement('div');
        let classText = document.createElement('h4');
        classText.innerHTML = `Class name: ${classes[x].class_name}`;
        let teacherText = document.createElement('h4');
        teacherText.innerHTML = `Teacher(s): ${classes[x].teacher(s)}`;
        let roomText = document.createElement('h4');
        roomText.innerHTMl = `Room: ${classes[x].room}`;
        let periodText = document.createElement('h4');
        periodText.innerHTML = `Periods: ${classes[x].periods}`;
        let semesterText = document.createElement('h4');
        semesterText.innerHTML = `Semesters: ${classes[x].semesters}`;
        let figure = document.createElement('figure');
        figure.appendChild(classText);
        figure.appendChild(teacherText);
        figure.appendChild(roomText);
        figure.appendChild(periodText);
        figure.appendChild(semesterText)
        classInfo.appendChild(figure);

    }
}*/
const options = ["Painting 2", "Math", "Science", "English"];
document.addEventListener("DOMContentLoaded", function () {
    const inputs = document.querySelectorAll(".class-input");
    const dropdownContainer = document.getElementById("dropdown-container");
    inputs.forEach(input => {
        const dropdown = document.createElement("select");
        dropdown.size = 6;
        dropdown.style.display = "none";
        function updateDropdown(filter) {
            dropdown.innerHTML = "";
            options
                .filter(option => option.toLowerCase().includes(filter.toLowerCase()))
                .forEach(option => {
                    const opt = document.createElement("option");
                    opt.value = option;
                    opt.textContent = option;
                    dropdown.appendChild(opt);
                });
            dropdown.style.display = dropdown.children.length ? "block" : "none";
        }
        input.addEventListener("input", () => updateDropdown(input.value));
        dropdown.addEventListener("change", function () {
            input.value = dropdown.value;
            dropdown.style.display = "none";
        });
        input.addEventListener("focus", function () {
            updateDropdown(input.value);
            dropdownContainer.appendChild(dropdown);
            dropdown.style.position = "absolute";
            dropdown.style.left = `${input.getBoundingClientRect().left}px`;
            dropdown.style.top = `${input.getBoundingClientRect().bottom + window.scrollY}px`;
        });
        input.addEventListener("blur", function () {
            setTimeout(() => dropdown.style.display = "none", 200);
        });
    });
});