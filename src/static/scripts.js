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
const options = ['ACAPELLA CHOIR*', 'ACCELERATED READING', 'ACCOUNTING 1', 'ADV MATH LAB', 'ADVANCED COMPUTER PROGRAMMING* - Concurrent Enrollment', 'ADVANCED CULINARY* - Concurrent Enrollment', "ADVANCED MEN'S ENSEMBLE*", 'ADVANCED WEIGHTS', "ADVANCED WOMEN'S ENSEMBLE*", 'ALGORITHMS & DATA STRUCTURES* - Concurrent Enrollment', 'AMERICAN STUDIES*', 'ANCIENT WORLD HISTORY', 'ANIMAL SCIENCE 1*', 'ANIMAL SCIENCE 2*', 'AP ART HISTORY*', 'AP ART-2D PORTFOLIO or AP ART DRAWING*', 'AP ART-3D SCULPTURE PORTFOLIO*', 'AP BIOLOGY - Concurrent Enrollment BIO 1610*', 'AP CALCULUS AB*', 'AP CALCULUS BC*', 'AP CHEMISTRY*', 'AP CHINESE*', 'AP ENGLISH LANGUAGE*', 'AP ENGLISH LITERATURE*', 'AP ENVIRONMENTAL SCIENCE-Concurrent Enrollment*', 'AP GOV & POLITICS*', 'AP GOV & POLITICS-Concurrent Enrollment*', 'AP HUMAN GEOGRAPHY*', 'AP MUSIC THEORY*', 'AP PHYSICS C*', 'AP PSYCHOLOGY*', 'AP SPANISH LANGUAGE*', 'AP STATISTICS*', 'AP US HISTORY - Concurrent Enrollment*', 'AP WORLD HISTORY*', 'ART HONORS*', 'ASL 1*', 'ASL 2*', 'ASL 3* - Concurrent Enrollment', 'ASL3* & ASL 4* - Concurrent Enrollment', 'ASTRONOMY - Concurrent Enrollment', 'ATHLETIC TRAINING PRACTICUM*', 'AUDIO PROD 1', 'BAKING & PASTRY', 'BASEBALL TEAM', 'BIOLOGY 1010 - Concurrent Enrollment*', 'BIOLOGY*', 'BOYS BASKETBALL TEAM', 'BOYS GOLF TEAM', 'BROADCASTING 1', 'BUILDING CONSTRUCTION* - Concurrent Enrollment', 'BUSINESS MANAGEMENT - Concurrent Enrollment', 'BUSINESS OFFICE SPECIALIST - Concurrent Enrollment', 'CALCULUS AB LAB', 'CERAMICS 1', 'CERAMICS 2', 'CHAMBER CHOIR - MADRIGAL*', 'CHAMBER ORCHESTRA*', 'CHEER TEAM*', 'CHEMISTRY 1010 - Concurrent Enrollment*', 'CHEMISTRY*', 'CHEVALIERS-DRILL TEAM*', 'CHILD DEVELOPMENT', 'CHINESE 1*', 'CHINESE 2*', 'CHINESE 3* - Concurrent Enrollment', 'CHINESE BRIDGE 3118*', 'COLLEGE/AP STUDY HALL', 'COMMERCIAL PHOTO 1', 'COMPUTER PROGRAMMING 1&2* - Concurrent Enrollment', 'CONCERT ORCHESTRA*', 'CREATIVE WRITING 1', 'CULINARY BASICS', 'CURRENT ISSUES', 'DANCE 3 Concurrent Enrollment -SYNERGY*', 'DANCE COMPANY*', 'DEBATE*', 'DESIGN SEWING 1 & 2', 'DIGITAL CURRICULUM', 'DIGITAL TECHNOLOGY - Concurrent Enrollment', 'DRAWING 1', 'DRAWING 2', 'DRUM SET 1', 'EARTH SCIENCE*', 'EMERGENCY MEDICAL RESPONDER - Concurrent Enrollment', 'ENGINEERING PRINCIPLES 1', 'ENGLISH 10 HONORS*', 'ENGLISH 10*', 'ENGLISH 1010 - Concurrent Enrollment', 'ENGLISH 11 HONORS*', 'ENGLISH 11*', 'ENGLISH 12*', 'ENGLISH ESSENTIALS', 'ENGLISH LANGUAGE DEVELOPMENT', 'ENTREPRENEURSHIP', 'ENVIRONMENTAL SCIENCE', 'Essentials Coordinator', 'FASHION DESIGN STUDIO', 'FILM LITERATURE', 'FINANCIAL LITERACY', 'FINANCIAL LITERACY - Concurrent Enrollment', 'FLORAL DESIGN 1', 'FLORAL DESIGN ADV', 'FOUNDATIONS OF NUTRITION-Concurrent Enrollment', 'FRENCH 1*', 'FRENCH 2*', 'FRENCH 3*', 'FRENCH 3* - Concurrent Enrollment', 'FRENCH 4/AP*', 'FRENCH 4/AP* - Concurrent Enrollment', 'GAME DEVELOPMENT FUNDAMENTALS 1', 'GENETICS', 'GERMAN 1*', 'GERMAN 2*', 'GERMAN 3* - Concurrent Enrollment', 'GERMAN 4/AP* - Concurrent Enrollment', 'GIRLS BASKETBALL TEAM', 'GIRLS SOCCER TEAM', 'GIRLS VOLLEYBALL TEAM', 'GOV & CIT', 'GRAPHIC DESIGN / DIGITAL MEDIA', 'GUITAR 1', 'HEALTH', 'HIGH FIT/ZUMBA', 'HISTORY OF ROCK AND ROLL - Concurrent Enrollment', 'HUMANITIES', 'ILLUSTRATION', 'INTERIOR DESIGN 1', 'INTERIOR DESIGN 3*', 'INTERNSHIP', 'INTRO TO BASKETBALL', 'INTRO TO PHYSICAL THERAPY*', 'ITALIAN 1*', 'ITALIAN 2*', 'JAZZ BAND 1*', 'JAZZ BAND 2*', 'JOURNALISM*', 'LAW ENFORCEMENT', 'LIFE SKILLS*', 'LIFETIME ACTIVITY', 'LONE PEAK LIVE', 'LONE PEAK LIVE - Concurrent Enrollment', 'LS MATH*', 'LS READING*', 'LS WRITING*', 'MATH 1010-Concurrent Enrollment', 'MATH DECISION MAKING*', 'MATH ESSENTIALS', 'MEDICAL ANATOMY & PHYSIOLOGY*', 'MEDICAL FORENSICS* - Concurrent Enrollment', 'MEDICAL TERMINOLOGY - Concurrent Enrollment', 'MOTION PICTURE', 'MUSIC APPRECIATION - Concurrent Enrollment', 'MUSICAL THEATER', 'MYTHOLOGY ANCIENT', 'PAINTING 1', 'PAINTING 2', 'PE FITNESS', 'PEOPLE OF THE PACIFIC', 'PERCUSSION ADV.*', 'PERCUSSION BEGINNING & INT.*', 'PHYSICS 1010 -Concurrent Enrollment*', 'PHYSICS*', 'PLANT AND SOIL SCIENCE 1*', 'POP CULTURE', 'POP CULTURE IN US - TAYLOR SWIFT', 'POP/ROCK ENSEMBLE*', 'POPULAR LITERATURE', 'POSITIVE PSYCHOLOGY', 'PRECALCULUS*', 'PRESCHOOL(EARLY CHILDHOOD EDUCATION 1&3)', 'PSYCHOLOGY', 'READING SKILLS', 'RESOURCE ENGLISH*', 'ROBOTICS 1', 'SCI FI / FANTASY', 'SCIENCE ESSENTIALS', 'SCRIPT WRITING', 'SCULPTURE 1', 'SCULPTURE 2', 'SECONDARY MATH 1 LAB', 'SECONDARY MATH 1*', 'SECONDARY MATH 2 EXTENDED*', 'SECONDARY MATH 2 LAB', 'SECONDARY MATH 2*', 'SECONDARY MATH 3 EXTENDED*', 'SECONDARY MATH 3 LAB', 'SECONDARY MATH 3*', 'SEMINARY', 'SOCIAL STUDIES ESSENTIALS', 'SOCIOLOGY', 'SPANISH 1*', 'SPANISH 2 HONORS*', 'SPANISH 2*', 'SPANISH 3 HONORS* - Concurrent Enrollment', 'SPANISH 3* - Concurrent Enrollment', 'SPANISH 4* - Concurrent Enrollment', 'SPORTS MEDICINE* - Concurrent Enrollment', 'SPORTS PSYCHOLOGY', 'STAGE CREW*', 'STEEL DRUMS', 'STUDENT GOVERNMENT*', 'STUDY HALL', 'SWIM TEAM', 'SYMPHONIC ORCHESTRA*', 'TEACHING K-12 Fall - Concurrent Enrollment', 'THE U.S. & WW II', 'THEATER PRODUCTIONS*', 'UKNIGHTED*', 'UKULELE', 'UNIFIED PE', 'URBAN DANCE/HIP-HOP', 'US HISTORY*', 'UVU LIVE INTERACTIVE', 'VIDEO CAPSTONE*', 'VIDEO CINEMATOGRAPHY', 'VIDEO EDITING', 'VIDEO PROD 1', 'WEATHER/CLIMATE - Concurrent Enrollment', 'WEB DEVELOPMENT 2 - Concurrent Enrollment', 'WEIGHTS', 'WEIGHTS Female', 'WILDLIFE BIOLOGY', 'WIND ENSEMBLE ADVANCED*', 'WIND SYMPHONY*', 'YEARBOOK*', 'YOGA 1'];
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