var subjectObject = {
    "Ανατολικής Μακεδονίας και Θράκης": {
        "Δράμας": [],
        "Έβρου": [],
        "Καβάλας": [],
        "Ροδόπης": [],
        "Ξάνθης": [],
    },
    "Κεντρικής Μακεδονίας": {
        "Ημαθίας": [],
        "Θεσσαλονίκης": [],
        "Κιλκίς": [],
        "Πέλλας": [],
        "Πιερίας": [],
        "Σερρών": [],
        "Χαλκιδικής": [],
    },
    "Δυτικής Μακεδονίας": {
        "Γρεβενών": [],
        "Καστοριάς": [],
        "Κοζάνης": [],
        "Φλώρινας": [],
    },
    "Ηπείρου": {
        "Άρτας": [],
        "Θεσπρωτίας": [],
        "Ιωαννίνων": [],
        "Πρεβεζας": [],
    },
    "Θεσσαλίας": {
        "Καρδίτσας": [],
        "Λάρισας": [],
        "Μαγνησίας": [],
        "Τρικάλων": [],
    },
    "Ιονίων Νήσων": {
        "Ζακύνθου": [],
        "Κέρκυρας": [],
        "Κεφαλληνίας": [],
        "Λευκάδας": [],
    },
    "Δυτικής Ελλάδας": {
        "Αιτολοακαρνανίας": [],
        "Αχαΐας": [],
        "Ηλείας": [],
    },
    "Στερεάς Ελλάδας": {
        "Βοιωτίας": [],
        "Ευβοίας": [],
        "Ευρυτανίας": [],
        "Φωκίδας": [],
        "Φθιώτιδας": []
    },
    "Αττικής": {
        "Αθηνών": [],
        "Ανατολικής Αττικής": [],
        "Δυτικής Αττικής": [],
        "Πειραιά": [],
    },
    "Πελοποννήσου": {
        "Αργολίδας": [],
        "Αρκαδίας": [],
        "Κορινθίας": [],
        "Λακωνίας": [],
        "Μεσσηνιας": []
    },
    "Βορείου Αιγαίου": {
        "Λέσβου": [],
        "Σάμου": [],
        "Χίου": [],
    },
    "Νοτίου Αιγαίου": {
        "Δωδεκανήσου": [],
        "Κυκλάδων": [],
    },
    "Κρήτης": {
        "Ηρακλείου": [],
        "Λασιθίου": [],
        "Ρεθύμνης": [],
        "Χανίων": [],
    },
}

var greenhousesNumber = {
    "1": [],
    "2": [],
    "3": [],
    "4": [],
    "5": [],
    "6": [],
    "7": [],
    "8": [],
}

var cultivation = {
    "Τριαντάφυλλο": [],
    "Μαργαρίτα": [],
    "Γυψοφύλλη": [],
    "Ντομάτα": [],
    "Αγγούρι": [],
    "Πιπεριά": [],
    "Ντομάτα": [],
    "Μπρόκολο": [],
    "Μαρούλι": []
}
window.onload = function () {
    var regionSel = document.getElementById("region");
    var prefectureSel = document.getElementById("prefecture");
    // var chapterSel = document.getElementById("chapter");
    for (var x in subjectObject) {
        regionSel.options[regionSel.options.length] = new Option(x, x);
    }
    regionSel.onchange = function () {
        //empty Chapters- and Topics- dropdowns
        // chapterSel.length = 1;
        prefectureSel.length = 1;
        //display correct values
        for (var y in subjectObject[this.value]) {
            prefectureSel.options[prefectureSel.options.length] = new Option(y, y);
        }
    }

    var numberSel = document.getElementById("greenhouse_number");
    for (var x in greenhousesNumber) {
        numberSel.options[numberSel.options.length] = new Option(x, x);
    }

    var cultSel = document.getElementById("cultivation");
    for (var x in cultivation) {
        cultSel.options[cultSel.options.length] = new Option(x, x);
    }

    var names = ["first_name", "last_name", "email"],
        fields = {};
    for (var i = 0; i < names.length; i++) {
        var fieldSet = document.getElementsByName(names[i]);
        if (fieldSet.length == 2) {
            fields[names[i]] = fieldSet[1];
            if (fieldSet[0].type.indexOf("select") != -1) {
                fieldSet[0].onchange = function () {
                    fields[this.name].selectedIndex = this.selectedIndex;
                }
            } else fieldSet[0].onkeyup = function () {
                fields[this.name].value = this.value;
            }
        }
    }
}