window.onload = function () {
    const options = [
        "ACAPELLA CHOIR*",
        "ACCELERATED READING",
        "ACCOUNTING 1",
        "ADV MATH LAB",
        "ADVANCED COMPUTER PROGRAMMING* - Concurrent Enrollment",
        "ADVANCED CULINARY* - Concurrent Enrollment",
        "ADVANCED MEN'S ENSEMBLE*",
        "ADVANCED WEIGHTS",
        "ADVANCED WOMEN'S ENSEMBLE*",
        "ALGORITHMS & DATA STRUCTURES* - Concurrent Enrollment",
        "AMERICAN STUDIES*",
        "ANCIENT WORLD HISTORY",
        "ANIMAL SCIENCE 1*",
        "ANIMAL SCIENCE 2*",
        "AP ART HISTORY*",
        "AP ART-2D PORTFOLIO or AP ART DRAWING*",
        "AP ART-3D SCULPTURE PORTFOLIO*",
        "AP BIOLOGY - Concurrent Enrollment BIO 1610*",
        "AP CALCULUS AB*",
        "AP CALCULUS BC*",
        "AP CHEMISTRY*",
        "AP CHINESE*",
        "AP ENGLISH LANGUAGE*",
        "AP ENGLISH LITERATURE*",
        "AP ENVIRONMENTAL SCIENCE-Concurrent Enrollment*",
        "AP GOV & POLITICS*",
        "AP GOV & POLITICS-Concurrent Enrollment*",
        "AP HUMAN GEOGRAPHY*",
        "AP MUSIC THEORY*",
        "AP PHYSICS C*",
        "AP PSYCHOLOGY*",
        "AP SPANISH LANGUAGE*",
        "AP STATISTICS*",
        "AP US HISTORY - Concurrent Enrollment*",
        "AP WORLD HISTORY*",
        "ART HONORS*",
        "ASL 1*",
        "ASL 2*",
        "ASL 3* - Concurrent Enrollment",
        "ASL3* & ASL 4* - Concurrent Enrollment",
        "ASTRONOMY - Concurrent Enrollment",
        "ATHLETIC TRAINING PRACTICUM*",
        "AUDIO PROD 1",
        "BAKING & PASTRY",
        "BASEBALL TEAM",
        "BIOLOGY 1010 - Concurrent Enrollment*",
        "BIOLOGY*",
        "BOYS BASKETBALL TEAM",
        "BOYS GOLF TEAM",
        "BROADCASTING 1",
        "BUILDING CONSTRUCTION* - Concurrent Enrollment",
        "BUSINESS MANAGEMENT - Concurrent Enrollment",
        "BUSINESS OFFICE SPECIALIST - Concurrent Enrollment",
        "CALCULUS AB LAB",
        "CERAMICS 1",
        "CERAMICS 2",
        "CHAMBER CHOIR - MADRIGAL*",
        "CHAMBER ORCHESTRA*",
        "CHEER TEAM*",
        "CHEMISTRY 1010 - Concurrent Enrollment*",
        "CHEMISTRY*",
        "CHEVALIERS-DRILL TEAM*",
        "CHILD DEVELOPMENT",
        "CHINESE 1*",
        "CHINESE 2*",
        "CHINESE 3* - Concurrent Enrollment",
        "CHINESE BRIDGE 3118*",
        "COLLEGE/AP STUDY HALL",
        "COMMERCIAL PHOTO 1",
        "COMPUTER PROGRAMMING 1&2* - Concurrent Enrollment",
        "CONCERT ORCHESTRA*",
        "CREATIVE WRITING 1",
        "CULINARY BASICS",
        "CURRENT ISSUES",
        "DANCE 3 Concurrent Enrollment -SYNERGY*",
        "DANCE COMPANY*",
        "DEBATE*",
        "DESIGN SEWING 1 & 2",
        "DIGITAL CURRICULUM",
        "DIGITAL TECHNOLOGY - Concurrent Enrollment",
        "DRAWING 1",
        "DRAWING 2",
        "DRUM SET 1",
        "EARTH SCIENCE*",
        "EMERGENCY MEDICAL RESPONDER - Concurrent Enrollment",
        "ENGINEERING PRINCIPLES 1",
        "ENGLISH 10 HONORS*",
        "ENGLISH 10*",
        "ENGLISH 1010 - Concurrent Enrollment",
        "ENGLISH 11 HONORS*",
        "ENGLISH 11*",
        "ENGLISH 12*",
        "ENGLISH ESSENTIALS",
        "ENGLISH LANGUAGE DEVELOPMENT",
        "ENTREPRENEURSHIP",
        "ENVIRONMENTAL SCIENCE",
        "Essentials Coordinator",
        "FASHION DESIGN STUDIO",
        "FILM LITERATURE",
        "FINANCIAL LITERACY",
        "FINANCIAL LITERACY - Concurrent Enrollment",
        "FLORAL DESIGN 1",
        "FLORAL DESIGN ADV",
        "FOUNDATIONS OF NUTRITION-Concurrent Enrollment",
        "FRENCH 1*",
        "FRENCH 2*",
        "FRENCH 3*",
        "FRENCH 3* - Concurrent Enrollment",
        "FRENCH 4/AP*",
        "FRENCH 4/AP* - Concurrent Enrollment",
        "GAME DEVELOPMENT FUNDAMENTALS 1",
        "GENETICS",
        "GERMAN 1*",
        "GERMAN 2*",
        "GERMAN 3* - Concurrent Enrollment",
        "GERMAN 4/AP* - Concurrent Enrollment",
        "GIRLS BASKETBALL TEAM",
        "GIRLS SOCCER TEAM",
        "GIRLS VOLLEYBALL TEAM",
        "GOV & CIT",
        "GRAPHIC DESIGN / DIGITAL MEDIA",
        "GUITAR 1",
        "HEALTH",
        "HIGH FIT/ZUMBA",
        "HISTORY OF ROCK AND ROLL - Concurrent Enrollment",
        "HUMANITIES",
        "ILLUSTRATION",
        "INTERIOR DESIGN 1",
        "INTERIOR DESIGN 3*",
        "INTERNSHIP",
        "INTRO TO BASKETBALL",
        "INTRO TO PHYSICAL THERAPY*",
        "ITALIAN 1*",
        "ITALIAN 2*",
        "JAZZ BAND 1*",
        "JAZZ BAND 2*",
        "JOURNALISM*",
        "LAW ENFORCEMENT",
        "LIFE SKILLS*",
        "LIFETIME ACTIVITY",
        "LONE PEAK LIVE",
        "LONE PEAK LIVE - Concurrent Enrollment",
        "LS MATH*",
        "LS READING*",
        "LS WRITING*",
        "MATH 1010-Concurrent Enrollment",
        "MATH DECISION MAKING*",
        "MATH ESSENTIALS",
        "MEDICAL ANATOMY & PHYSIOLOGY*",
        "MEDICAL FORENSICS* - Concurrent Enrollment",
        "MEDICAL TERMINOLOGY - Concurrent Enrollment",
        "MOTION PICTURE",
        "MUSIC APPRECIATION - Concurrent Enrollment",
        "MUSICAL THEATER",
        "MYTHOLOGY ANCIENT",
        "PAINTING 1",
        "PAINTING 2",
        "PE FITNESS",
        "PEOPLE OF THE PACIFIC",
        "PERCUSSION ADV.*",
        "PERCUSSION BEGINNING & INT.*",
        "PHYSICS 1010 -Concurrent Enrollment*",
        "PHYSICS*",
        "PLANT AND SOIL SCIENCE 1*",
        "POP CULTURE",
        "POP CULTURE IN US - TAYLOR SWIFT",
        "POP/ROCK ENSEMBLE*",
        "POPULAR LITERATURE",
        "POSITIVE PSYCHOLOGY",
        "PRECALCULUS*",
        "PRESCHOOL(EARLY CHILDHOOD EDUCATION 1&3)",
        "PSYCHOLOGY",
        "READING SKILLS",
        "RESOURCE ENGLISH*",
        "ROBOTICS 1",
        "SCI FI / FANTASY",
        "SCIENCE ESSENTIALS",
        "SCRIPT WRITING",
        "SCULPTURE 1",
        "SCULPTURE 2",
        "SECONDARY MATH 1 LAB",
        "SECONDARY MATH 1*",
        "SECONDARY MATH 2 EXTENDED*",
        "SECONDARY MATH 2 LAB",
        "SECONDARY MATH 2*",
        "SECONDARY MATH 3 EXTENDED*",
        "SECONDARY MATH 3 LAB",
        "SECONDARY MATH 3*",
        "SEMINARY",
        "SOCIAL STUDIES ESSENTIALS",
        "SOCIOLOGY",
        "SPANISH 1*",
        "SPANISH 2 HONORS*",
        "SPANISH 2*",
        "SPANISH 3 HONORS* - Concurrent Enrollment",
        "SPANISH 3* - Concurrent Enrollment",
        "SPANISH 4* - Concurrent Enrollment",
        "SPORTS MEDICINE* - Concurrent Enrollment",
        "SPORTS PSYCHOLOGY",
        "STAGE CREW*",
        "STEEL DRUMS",
        "STUDENT GOVERNMENT*",
        "STUDY HALL",
        "SWIM TEAM",
        "SYMPHONIC ORCHESTRA*",
        "TEACHING K-12 Fall - Concurrent Enrollment",
        "THE U.S. & WW II",
        "THEATER PRODUCTIONS*",
        "UKNIGHTED*",
        "UKULELE",
        "UNIFIED PE",
        "URBAN DANCE/HIP-HOP",
        "US HISTORY*",
        "UVU LIVE INTERACTIVE",
        "VIDEO CAPSTONE*",
        "VIDEO CINEMATOGRAPHY",
        "VIDEO EDITING",
        "VIDEO PROD 1",
        "WEATHER/CLIMATE - Concurrent Enrollment",
        "WEB DEVELOPMENT 2 - Concurrent Enrollment",
        "WEIGHTS",
        "WEIGHTS Female",
        "WILDLIFE BIOLOGY",
        "WIND ENSEMBLE ADVANCED*",
        "WIND SYMPHONY*",
        "YEARBOOK*",
        "YOGA 1",
    ];
    const teachers = [
        "ASAY",
        "BANKS^",
        "BERRETT",
        "BERRY",
        "BEZZANT",
        "BIRRELL",
        "BRAUN",
        "BRINKERHOFF, E.",
        "BRINKERHOFF, L.",
        "BROADBENT",
        "BRYAN^",
        "BURDETT",
        "BURNETT^^",
        "CARPENTER",
        "COATNEY",
        "COX, B.^",
        "COX, C.^",
        "COX, C.^^",
        "CRAFT",
        "DAVENPORT (BRANCH)",
        "DAY^",
        "DILELLO^^",
        "DULONG",
        "DURRANT",
        "ELMER",
        "EREKSON",
        "FARR^",
        "FERRAN",
        "FIELD",
        "FITZPATRICK",
        "FLOOD",
        "GIBBY^",
        "GUMMOW",
        "GUNNARSON",
        "HARLOW",
        "HAYNIE",
        "HEATH",
        "HOPE",
        "HUBBARD",
        "HURTT^",
        "IKA^^",
        "JARVIE",
        "JAYNES",
        "JENSEN^",
        "JOLLEY^",
        "KIM, H.",
        "KIM, J.",
        "KNIGHT^",
        "LEE^",
        "LYONS",
        "MCPHERSON",
        "MITCHELL^",
        "MOEA'I (DICKSON)",
        "MOLENI",
        "MOLEN^",
        "MONTROSE^",
        "MURPHY^",
        "MURRAY",
        "NAIR",
        "NELSON",
        "NIELSON",
        "OMER, R.",
        "PACK^^",
        "PASKETT^^",
        "PASSEY",
        "PAXTON^^",
        "PEARSON",
        "PEAY",
        "PERKES",
        "POWELL",
        "REES",
        "RIDGWAY",
        "ROSS",
        "RUCHTI",
        "SCHETTLER",
        "SCHOONOVER",
        "SEELY",
        "SEMINARY FACULTY",
        "SMITH, CALVIN^^",
        "SMITH, CASSIDY",
        "SMITH, CRAIG",
        "SMITH, WESLEY",
        "SPENCER^",
        "SPRINGER",
        "SUMMERS",
        "SWARTZ",
        "TALBERT",
        "TERRY",
        "TIFFANY",
        "TOPHAM^",
        "TRACY",
        "TURNER",
        "VAN WOERKOM^",
        "VERNON",
        "VOORHEIS^",
        "WAHLIN",
        "WALKER, M.",
        "WALLACE",
        "WARNER",
        "WAWRO^",
        "WENTZ",
        "WHATCOTT",
        "WILY",
        "WINN",
    ];
    let results = window.scheduleResults || [];
    let currentIndex = 0;
    document.getElementById("autofill-btn").addEventListener("click", () => {
        const testData = [
            "SPANISH 3* - Concurrent Enrollment",
            "CALCULUS AB LAB",
            "SPANISH 4* - Concurrent Enrollment",
            "AP SPANISH LANGUAGE*",
            "ART HONORS*",
            "PAINTING 2",
            "DRAWING 1",
            "MATH 1010-Concurrent Enrollment"
        ];
        const testTeachers = [
            "PEAY",
            "SUMMERS",
            "PEAY",
            "PEAY"
        ];
        testData.forEach((x, i) => {
            let e = document.querySelector(`.class-input[name="class${i + 1}"]`);
            if (e) e.value = x;
        });
        testTeachers.forEach((x, i) => {
            let e = document.querySelector(`.teacher-input[name="teacher${i + 1}"]`);
            if (e) e.value = x;
        });
    });
    function updateScheduleDisplay() {
        if (results.length > 0) {
            const scheduleBox = document.querySelector("#schedule-box");
            const scheduleDisplay = document.querySelector("#schedule-display");
            scheduleDisplay.innerHTML = Object.entries(results[currentIndex])
                .map(
                    ([period, { class_name, teachers }]) =>
                        `<p>Period ${period}: ${class_name} (Teachers: ${teachers.join(
                            ", "
                        )})</p>`
                )
                .join("");
            scheduleBox.style.display = "block";
        }
    }
    if (results.length > 0) {
        const prevBtn = document.querySelector("#prev-btn");
        const nextBtn = document.querySelector("#next-btn");
        prevBtn.addEventListener("click", function () {
            if (currentIndex > 0) {
                currentIndex--;
                updateScheduleDisplay();
            }
        });
        nextBtn.addEventListener("click", function () {
            if (currentIndex < results.length - 1) {
                currentIndex++;
                updateScheduleDisplay();
            }
        });
        updateScheduleDisplay();
    }
    const inputs = document.querySelectorAll(".class-input");
    const dropdownContainer = document.getElementById("dropdown-container");
    inputs.forEach((input) => {
        const dropdown = document.createElement("select");
        dropdown.size = 6;
        dropdown.style.display = "none";
        function updateDropdown(filter) {
            dropdown.innerHTML = "";
            options
                .filter((option) => option.toLowerCase().includes(filter.toLowerCase()))
                .forEach((option) => {
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
            dropdown.style.top = `${input.getBoundingClientRect().bottom + window.scrollY
                }px`;
        });
        input.addEventListener("blur", function () {
            setTimeout(() => (dropdown.style.display = "none"), 200);
        });
    });
    const tinputs = document.querySelectorAll(".teacher-input");
    tinputs.forEach((tinput) => {
        const dropdown = document.createElement("select");
        dropdown.size = 6;
        dropdown.style.display = "none";
        function updateDropdown(filter) {
            dropdown.innerHTML = "";
            teachers
                .filter((teacher) =>
                    teacher.toLowerCase().includes(filter.toLowerCase())
                )
                .forEach((teacher) => {
                    const teach = document.createElement("option");
                    teach.value = teacher;
                    teach.textContent = teacher;
                    dropdown.appendChild(teach);
                });
            dropdown.style.display = dropdown.children.length ? "block" : "none";
        }
        tinput.addEventListener("input", () => updateDropdown(tinput.value));
        dropdown.addEventListener("change", function () {
            tinput.value = dropdown.value;
            dropdown.style.display = "none";
        });
        tinput.addEventListener("focus", function () {
            updateDropdown(tinput.value);
            dropdownContainer.appendChild(dropdown);
            dropdown.style.position = "absolute";
            dropdown.style.left = `${tinput.getBoundingClientRect().left}px`;
            dropdown.style.top = `${tinput.getBoundingClientRect().bottom + window.scrollY
                }px`;
        });
        tinput.addEventListener("blur", function () {
            setTimeout(() => (dropdown.style.display = "none"), 200);
        });
    });
};
