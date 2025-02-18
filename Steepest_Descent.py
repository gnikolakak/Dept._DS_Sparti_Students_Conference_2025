# Ο κώδικας υλοποιεί τον Αλγόριθμο της Steepest Descent για την εύρεση του ελαχίστου μιας συνάρτησης δύο μεταβλητών
# Ο χρήστης εισάγει τα αρχικά σημεία, τις παραμέτρους και την συνάρτηση που θα ήθελε να εξετάσει
# Ο αλγόριθμος υπολογίζει τις παραγώγους και την κλίση της συνάρτησης, ενημερώνοντας τα σημεία σε κάθε βήμα
# Η διαδικασία τερματίζεται:
# 1) όταν ικανοποιηθεί ένα από τα κριτήρια τερματισμού (προτού ξεπεραστεί ο μέγιστος αριθμός επαναλήψεων) και έτσι εμφανίζονται τα αποτελέσματα και τα γραφήματα (σε τρισδιάστατη και δισδιάστατη μορφή) που δείχνουν την πορεία του αλγορίθμου
# 2) όταν ξεπεραστεί ο μέγιστος αριθμός επαναλήψεων ενημερώνοντας τον χρήστη πως ο αριθμός των επαναλήψεων ξεπεράστηκε χωρίς να εμφανιστούν οι γραφικές παραστάσεις

# Οι βιβλιοθήκες που χρησιμοποιούνται για την εκτέλεση του αλγορίθμου
import sympy as sp # Υπολογισμός συμβολικών πράξεων (π.χ. για εξισώσεις, για παραγώγους)
import numpy as np # Εκτέλεση μαθηματικών πράξεων
import matplotlib.pyplot as plt # Χρησιμοποιείται για την δημιουργία γραφημάτων και την απεικόνιση των αποτελεσμάτων

# Χρήση της συνάρτησης Initial_Point() για την είσοδο των αρχικών σημείων (x0,y0) από το χρήστη
def Initial_Point(): # Η συνάρτηση Initial_Point()
    while True: # Σε περίπτωση που ο χρήστης εισάγει μία τιμή που δεν είναι αριθμητική, ζητείται ξανά η είσοδος του σημείου, ενημερώνοντας τον χρήστη με αντίστοιχο μήνυμα
        try: # Θα εμφανιστεί στην οθόνη στην περίπτωση που ο χρήστης εισάγει αριθμητική τιμή
            print("Αρχικά σημεία & Ρυθμός εκμάθησης:") # Το μήνυμα εμφανίζεται αρχικά στην οθόνη του χρήστη
            x0 = float(input("Το x0 είναι το αρχικό σημείο. Παρακαλώ εισάγετε το x0: ")) # Είσοδος του σημείου x0 από τον χρήστη
            y0 = float(input("Το y0 είναι το αρχικό σημείο. Παρακαλώ εισάγετε το y0: ")) # Είσοδος του σημείου y0 από τον χρήστη
            return x0, y0 # Επιστρέφει τα x0, y0

        except ValueError: # Θα εμφανιστεί στην οθόνη στην περίπτωση που ο χρήστης εισάγει λανθασμένη είσοδο, δηλαδή μία μη αριθμητική τιμή
            print("Λάθος είσοδος! Παρακαλώ εισάγετε έγκυρους αριθμούς για x0 και y0.") # Για την προκειμένη περίπτωση, εμφανίζεται αντίστοιχο μήνυμα, ενημερώνοντας τον χρήστη και ζητώντας ξανά την είσοδο του σημείου που πληκτρολόγησε λάθος (χρήση της while True)

# Χρήση της συνάρτησης Parameters() για την είσοδο του a (ρυθμού εκμάθησης - learning rate) και των σταθερών c1,c2,c3 που τερματίζουν τον αλγόριθμο
def Parameters(): # Η συνάρτηση Parameters()
    while True: # Σε περίπτωση που ο χρήστης εισάγει μία τιμή που δεν είναι αριθμητική, ζητείται ξανά η είσοδος της αντίστοιχης παραμέτρου, ενημερώνοντας τον χρήστη με αντίστοιχο μήνυμα
        try: # Θα εμφανιστεί στην οθόνη σε περίπτωση που ο χρήστης εισάγει σωστή είσοδο (αριθμητική τιμή)
            a = float(input("Το a είναι το learning rate. Παρακαλώ εισάγετε το a: ")) # Είσοδος του ρυθμού εκμάθησης (το πόσο γρήγορα προχωρά η μέθοδος προς την κατεύθυνση του ελαχίστου) από τον χρήστη
            print("-------------------------------------------------------------------------------------")

            # Η λειτουργία του αλγορίθμου περιγράφεται στην επόμενη εντολή (print)
            print("Ο αλγόριθμος της Steepest Descent σταματά αν ένα από τα παρακάτω κριτήρια τερματισμού ικανοποιηθεί: \n"
            "1. Σε περίπτωση που ο αριθμός των επαναλήψεων ξεπεράσει τις 1000 και δεν έχει ικανοποιηθεί κάποιο από τα κριτήρια.\n"
            "2. Η κλίση της συνάρτησης στο σημείο που έχει βρεθεί είναι μικρότερη από μια σταθερά c1 την οποία ορίζει ο χρήστης. \n"
            " Αν η κλίση ισούται με 0 στο αρχικό σημείο (x0,y0), τότε ζητά από τον χρήστη να δώσει νέο αρχικό σημείο.\n"
            " 3. Η απόσταση μεταξύ δύο διαδοχικών σημείων να είναι μικρότερη από μια σταθερά c2 την οποία ορίζει ο χρήστης. \n"
            " 4. Η τιμή της συνάρτησης μεταξύ δύο διαδοχικών σημείων να είναι μικρότερη από μια σταθερά c3 την οποία ορίζει ο χρήστης. \n")
            print("-------------------------------------------------------------------------------------")

            # Είσοδος των σταθερών και περιγραφή της λειτουργίας των αντίστοιχων κριτηρίων τερματισμού
            print("Επομένως, για να προχωρήσει ο αλγόριθμός απαιτούνται τα c1, c2, c3 από τον χρήστη:")
            c1 = float(input("1ο) Ποιο το c1 ώστε να μπορεί να εξεταστεί το κριτήριο |∇f| ≤ c1;")) # Το πρώτο κριτήριο αφορά το όριο της κλίσης
            c2 = float(input("2ο) Ποιο το c2 ώστε να μπορεί να εξεταστεί το κριτήριο |Xn - Xn-1| ≤ c2; ")) # Το δεύτερο κριτήριο αφορά το όριο για την απόσταση μεταξύ δύο διαδοχικών σημείων
            c3 = float(input("3ο) Ποιο το c3 ώστε να μπορεί να εξεταστεί το κριτήριο |f(Xn) - f(Xn-1)| ≤ c3; ")) # Το τρίτο κριτήριο αφορά το όριο για την διαφορά μεταξύ των τιμών της συνάρτησης σε διαδοχικά σημεία
            return a, c1, c2, c3 # Επιστρέφει τα a, c1, c2, c3

        except ValueError: # Θα εμφανιστεί στην οθόνη στην περίπτωση που ο χρήστης εισάγει λανθασμένη είσοδο, δηλαδή μία είσοδο μη αριθμητική
            print("Λάθος είσοδος! Παρακαλώ εισάγετε έγκυρους αριθμούς.") # Για την προκειμένη περίπτωση, εμφανίζεται αντίστοιχο μήνυμα, ενημερώνοντας τον χρήστη και ζητώντας ξανά την είσοδο της παραμέτρου που πληκτρολόγησε λάθος (χρήση της while True)

# Χρήση της συνάρτησης f() προκειμένου ο χρήστης να εισάγει την συνάρτηση f(x,y) που επιθυμεί, η οποία θα ελαχιστοποιηθεί σε μορφή συμβολικών παραστάσεων
# Έτσι, επιστρέφει την συνάρτηση σε μορφή που μπορεί να επεξεργαστεί αλγεβρικά από την sympy
def f(): # Η συνάρτηση f()
    while True: # Σε περίπτωση που ο χρήστης εισάγει οτιδήποτε πέρα από εξίσωση, ζητείται ξανά η είσοδος της συνάρτησης, ενημερώνοντας τον χρήστη με αντίστοιχο μήνυμα
        try: # Θα εμφανιστεί στην οθόνη όταν ο χρήστης δώσει έγκυρη συνάρτηση (π.χ. 5*x + 4*y)
            print("-------------------------------------------------------------------------------------")
            expr_str = input("Παρακαλώ εισάγετε τη συνάρτηση σε μορφή x και y (π.χ., x**2 + y**4): ") # Εισαγωγή της συνάρτησης δύο μεταβλητών από τον χρήστη
            expr = sp.sympify(expr_str) # Μετατροπή της συμβολοσειράς (string) σε αλγεβρική παράσταση
            return expr # Επιστρέφει την αλγεβρική παράσταση

        except sp.SympifyError: # Θα εμφανιστεί στην οθόνη στην περίπτωση που ο χρήστης εισάγει μη έγκυρη συνάρτηση (π.χ. 5x + 4y)
            print("Λάθος είσοδος! Παρακαλώ εισάγετε έγκυρη συνάρτηση.") # Για την προκειμένη περίπτωση, εμφανίζεται αντίστοιχο μήνυμα, ενημερώνοντας τον χρήστη και ζητώντας ξανά την είσοδο έγκυρης συνάρτησης

# Υλοποίηση του αλγορίθμου της steepest_descent για την ελαχιστοποίηση μιας συνάρτησης δύο μεταβλητών
def steepest_descent(f_num, x0, y0, a, c1, c2, c3, derivative_x, derivative_y): # f_num: Η συνάρτηση προς ελαχιστοποίηση - μετατροπή της συμβολικής συνάρτησης σε αριθμητική με χρήση του lambdify από την sympy
    tries = 0 # tries: Αντιπροσωπεύει τον αριθμό των επαναλήψεων του αλγορίθμου, δηλαδή πόσες φορές ο αλγόριθμος θα επαναλάβει την διαδικασία για την συνάρτηση που έχει εισάγει ο χρήστης
    MAX_TRIES = 1000 # MAX_TRIES: Ο μέγιστος αριθμός επαναλήψεων. Αν ο αλγόριθμος δεν συγκλίνει πριν φτάσει σε αυτόν τον αριθμό, τότε θα τερματιστεί
    points = [] # points: Λίστα που αποθηκεύει τα σημεία που επισκέπτεται ο αλγόριθμος μέχρι να φτάσει στο τελικό σημείο ή το MAX_TRIES
    x, y = sp.symbols('x y') # sp: Από την βιβλιοθήκη sympy
    # symbols: Συνάρτηση της βιβλιοθήκης sympy, χρησιμοποιείται για την δημιουργία συμβολικών μεταβλητών, με τις μεταβλητές αυτές να μην είναι αριθμοί αλλά συμβολισμοί που χρησιμοποιούνται στις εξισώσεις
    # x, y: Η symbols επιστρέφει δύο συμβολικές μεταβλητές τις οποίες αποδίσει στις x, y
    # Έτσι, έχει δύο μεταβλητές οι οποίες μπορούν να χρησιμοποιηθούν στην παραγώγιση, στην επίλυση εξισώσεων κλπ

    x_path = [x0] # x_path: Λίστα που αποθηκεύει την τιμή του x κατά την πορεία του αλγορίθμου, ώστε να μπορεί να γίνει απεικόνιση
    y_path = [y0] # y_path: Λίστα που αποθηκεύει την τιμή του y κατά την πορεία του αλγορίθμου, ώστε να μπορεί να γίνει απεικόνιση
    z_path = [f_num(x0, y0)] # z_path: Λίστα που αποθηκεύει την τιμή του f(x, y) κατά την πορεία του αλγορίθμου, ώστε να μπορεί να γίνει απεικόνιση

    slope_x = derivative_x.subs({x: x0, y: y0}).evalf() # Υπολογίζεται η τιμή της παραγώγου στο σημείο (x0, y0), μετατρέπεται το αποτέλεσμα σε αριθμητική τιμή και αποθηκεύεται στην μεταβλητή slope_x
    # derivative_x: Η μερική παράγωγος της συνάρτησης ως προς την μεταβλητή x
    # .subs({x: x0, y: y0}): Μέθοδος η οποία χρησιμοποιείται για να αντικαταστήσει τις μεταβλητές x, y με τις τιμές x0, y0 αντίστοιχα
    # .evalf(): Μέθοδος η οποία μετατρέπει την συμβολική έκφραση σε αριθμητική τιμή και την επιστρέφει

    slope_y = derivative_y.subs({x: x0, y: y0}).evalf() # Κατά τον ίδιο τρόπο κι εδώ

    grad_norm = sp.sqrt(slope_x**2 + slope_y**2) # Υπολογίζεται το μέτρο του βαθμωτού το οποίο δείχνει πόσο γρήγορα αλλάζει η συνάρτηση στο σημείο που εξετάζουμε
    # grad_norm: Υπολογισμός του μέτρου (norm) του διανύσματος της κλίσης (gradient norm)
    # Αν είναι μηδέν, σημαίνει ότι η συνάρτηση είναι ήδη σε ένα τοπικό ελάχιστο ή μέγιστο
    # sp.sqrt: Υπολογισμός της τετραγωνικής ρίζας του αθροίσματος των τετραγώνων των παραγώγων

    slope_x_expr = derivative_x # Η τιμή της μερικής παραγώγου ως προς x, αποδίδεται στην μεταβλητή slope_x_expr
    slope_y_expr = derivative_y # Η τιμή της μερικής παραγώγου ως προς y, αποδίδεται στην μεταβλητή slope_y_expr
    slope_x = slope_x_expr.subs({x: x0, y: y0}).evalf() # Αντικατάσταση των x,y από τα x0,y0 & υπολογισμός της αριθμητικής τιμής της μερικής παραγώγου ως προς x στο σημείο (x0, y0)
    slope_y = slope_y_expr.subs({x: x0, y: y0}).evalf() # Αντικατάσταση των x,y από τα x0,y0 & υπολογισμός της αριθμητικής τιμής της μερικής παραγώγου ως προς y στο σημείο (x0, y0)
    print("Η μερική παράγωγος ως προς x:", slope_x_expr) # Εμφάνιση της μερικής παραγώγου ως προς x
    print("Η μερική παράγωγος ως προς y:", slope_y_expr) # Εμφάνιση της μερικής παραγώγου ως προς y

    # Σε περίπτωση που η κλίση είναι 0, ζητάμε από τον χρήστη να δώσει νέο x0 και y0
    while grad_norm == 0:
        print("Η κλίση στο σημείο (x0, y0) είναι 0. Παρακαλώ εισάγετε νέο σημείο εκκίνησης.")
        x0, y0 = Initial_Point() # Ο χρήστης δίνει ξανά τα νέα σημεία

        # Υπολογίζουμε ξανά τις παραγώγους και την κλίση στο νέο σημείο
        slope_x = derivative_x.subs({x: x0, y: y0}).evalf()
        slope_y = derivative_y.subs({x: x0, y: y0}).evalf()
        grad_norm = sp.sqrt(slope_x**2 + slope_y**2)

    # Όσο ο αλγόριθμος επαναλαμβάνει την διαδικασία και τερματίζεται μέχρι και τις 1000 επαναλήψεις
    while tries <= MAX_TRIES:
        # Υπολογισμός των παραγώγων και της κλίσης
        slope_x = derivative_x.subs({x: x0, y: y0}).evalf()
        slope_y = derivative_y.subs({x: x0, y: y0}).evalf()
        grad_norm = sp.sqrt(slope_x**2 + slope_y**2)

        # Προσθήκη του σημείου με συντεταγμένες (x0,y0) στην λίστα points με χρήση της μεθόδου append
        points.append((x0, y0))

        # ΚΡΙΤΗΡΙΑ ΤΕΡΜΑΤΙΣΜΟΥ
        # Κριτήριο 1 -> Έλεγχος αν η κλίση είναι μικρότερη από την σταθερά c1:
        # Αν είναι, διακόπτεται η διαδικασία και καταγράφεται το αποτέλεσμα στο criterion
        # Αν δεν είναι, ελέγχει αν υπάρχουν τουλάχιστον δύο σημεία στην λίστα points. Αν υπάρχουν, υπολογίζει την απόσταση του τελευταίου και του προτελευταίου σημείου, με βάση τον τύπο της ευκλείδιας απόστασης
        if grad_norm < c1: # grad_norm: η τιμή της κλίσης. Αν η τιμή της κλίσης είναι μικρότερη από την σταθερά c1 που έχει οριστεί παραπάνω, τότε ο αλγόριθμος προχωρά στις επόμενες εντολές αφού ικανοποιείται το 1ο κριτήριο
            criterion = "1ο κριτήριο: Η κλίση είναι μικρή." # Αν η παραπάνω συνθήκη είναι αληθής, τότε στη μεταβλητή criterion, ανατίθεται η τιμή "1ο κριτήριο: Η κλίση είναι μικρή.", με την οποία αναγνωρίζεται πως το 1ο κριτήριο έχει ικανοποιηθεί
            break # Αν ισχύουν τα παραπάνω, τότε σταματά η εκτέλεση του βρόχου και η διαδικασία ολοκληρώνεται

        elif len(points) > 1: # Αν το πρώτο κριτήριο δεν ικανοποιείται, εξετάζεται η περίπτωση η τιμή της κλίσης να είναι μεγαλύτερη από την σταθερά c1
            prev_x, prev_y = points[-2] # points[-2]: Αναφέρεται στο δεύτερο από το τέλος στοιχείο της λίστας points
            # Επομένως, η εντολή "prev_x, prev_y = points[-2]" αναθέτει τις συντεταγμένες του προτελευταίου σημείου της λίστας στις μεταβλητές prev_x, prev_y
            distance = sp.sqrt((x0 - prev_x)**2 + (y0 - prev_y)**2).evalf() # (x0 - prev_x)**2 + (y0 - prev_y)**2: Υπολογισμός του τετραγώνου της απόστασης μεταξύ δύο σημείων στον δισδιάστατο χώρο
            # .evalf(): Υπολογίζει την αριθμητική τιμή του αποτελέσματος, μετατρέποντας την συμβολική έκφραση σε δεκαδικό αριθμό και αποθηκεύεται στην μεταβλητή distance


            # Κριτήριο 2 -> Έλεγχος αν η απόσταση μεταξύ του τρέχοντος και του προτελευταίου σημείου είναι μικρότερη από την σταθερά c2:
            # Αν είναι, διακόπτεται η διαδικασία και καταγράφεται το αποτέλεσμα στο criterion
            # Αν δεν είναι, υπολογίζονται οι τιμές της συνάρτησης στο προτελευταίο και στο τρέχον σημείο και αποθηκεύονται στις μεταβλητές f_prev και f_current αντίστοιχα, προκειμένου να ολοκληρωθεί η διαδικασία της βελτιστοποίησης και να βρεθεί το ελάχιστο σημείο
            if distance < c2: # distance: Η απόσταση, μάς δείχνει πόσο μακριά είναι τα δύο σημεία στον δισδιάστατο χώρο (έχει υπολογιστεί παραπάνω)
            # Όταν η απόσταση δύο διαδοχικών σημείων είναι μικρότερη από την τιμή της σταθεράς c2 που έχει εισάγει ο χρήστης, τότε η συνθήκη είναι αληθής και τα σημεία είναι πολύ κοντά μεταξύ τους
                criterion = "2ο κριτήριο: Η απόσταση μεταξύ δύο διαδοχικών σημείων είναι μικρή." # Η τιμή "2ο κριτήριο: Η απόσταση μεταξύ δύο διαδοχικών σημείων είναι μικρή.", ανατίθεται στην μεταβλητή criterion
                break  # Αν ισχύουν τα παραπάνω, τότε σταματά η εκτέλεση του βρόχου και η διαδικασία ολοκληρώνεται

            f_prev = f_num(prev_x, prev_y) # Υπολογίζεται η τιμή της συνάρτησης f_num στο προτελευταίο σημείο (prev_x, prev_y), που είναι το προηγούμενο σημείο από το (x0, y0)
            # Η τιμή της συνάρτησης στο προτελευταίο σημείο αποθηκεύεται στην μεταβλητή f_prev
            f_current = f_num(x0, y0) # Υπολογίζεται η τιμή της συνάρτησης f_num στο τρέχον σημείο (x0, y0)
            # Η τιμή της συνάρτησης στο τρέχον σημείο αποθηκεύεται στη μεταβλητή f_current


            # Κριτήριο 3 -> Σύγκλιση της διαφοράς τιμών της συνάρτησης. Ελέγχει αν η απόλυτη διαφορά μεταξύ των τιμών μιας συνάρτησης σε δύο διαδοχικά σημεία είναι μικρότερη από την σταθερά c3:
            # Αν είναι, τότε η συνάρτηση έχει συγκλίνει και καταγράφεται το κριτήριο σύγκλισης
            if abs(f_current - f_prev) < c3: # abs(): Συνάρτηση απόλυτης τιμής
            # Εδώ, υπολογίζεται η απόλυτη διαφορά μεταξύ των τιμών της συνάρτησης σε δύο διαδοχικά σημεία
            # Αν η διαφορά αυτή είναι μικρότερη από την σταθερά c3, τότε δεν αλλάζει πολύ από το ένα σημείο στο άλλο
            # Αυτό σημαίνει πως η διαδικασία της βελτιστοποίησης πλησιάζει στο επιθυμητό αποτέλεσμα
                criterion = "3ο κριτήριο: Η σύγκλιση της συνάρτησης είναι μικρή." # Αν η παραπάνω συνθήκη είναι αληθής, τότε η τιμή "3ο κριτήριο: Η σύγκλιση της συνάρτησης είναι μικρή.", ανατίθεται στην μεταβλητή criterion
                break # Αν ισχύουν τα παραπάνω, τότε σταματά η εκτέλεση του βρόχου και η διαδικασία ολοκληρώνεται
                # Διακόπτεται η διαδικασία επειδή δεν υπάρχουν ουσιαστικές αλλαγές στις τιμές της συνάρτησης
            # Αυτό σημαίνει πως η διαδικασία έχει ολοκληρωθεί αφού οι τιμές της συνάρτησης δεν αλλάζουν σημαντικά πια
            # Έτσι, η συνάρτηση πλησιάζει στο σημείο ελαχίστου

        # Ενημέρωση μεταβλητών x0 και y0. Οι τιμές ενημερώνονται με βάση την κλίση και τον ρυθμό εκμάθησης (όπως αποδεικνύουν οι επόμενες πράξεις)
        x0 = x0 - a * slope_x
        y0 = y0 - a * slope_y

        x_path.append(x0) # Προσθήκη (append) της τρέχουσα τιμής του x, δηλαδή κάθε φορά του x0, στην λίστα x_path, ώστε η λίστα αυτή να περιέχει όλα τα σημεία x που επισκέπτεται ο αλγόριθμος σε όλη την διαδικασία
        # Έτσι, η λίστα προβάλλει τα σημεία που έχει περάσει το x καθώς πλησιάζει στο βέλτιστο
        y_path.append(y0) # Προσθήκη (append) της τρέχουσα τιμής του y, δηλαδή κάθε φορά του y0, στην λίστα y_path, ώστε η λίστα αυτή να περιέχει όλα τα σημεία y που επισκέπτεται ο αλγόριθμος σε όλη την διαδικασία
        # Έτσι, η λίστα προβάλλει τα σημεία που έχει περάσει το y καθώς πλησιάζει στο βέλτιστο
        z_path.append(f_num(x0, y0)) # Προσθήκη (append) των τιμών της συνάρτησης σε κάθε (τρέχον) σημείο (x0, y0) στην λίστα z_path
        # Με αυτό τον τρόπο, γνωρίζουμε πώς αλλάζει η τιμή της συνάρτησης καθώς πλησιάζουμε προς το βέλτιστο κατά την διάρκεια των επαναλήψεων του αλγορίθμου

        # Μετάβαση στον επόμενο κύκλο επανάληψης της διαδικασίας για τον έλεγχο επόμενων σημείων
        tries += 1

    # Σε περίπτωση που ο αλγόριθμος δεν καταφέρει να συγκλίνει σε κάποιο βέλτιστο σημείο μέσα στον καθορισμένο αριθμό επαναλήψεων, τότε υπάρχει αποτυχία
    if tries > MAX_TRIES: # Αν η διαδικασία για την εύρεση του ελαχίστου ξεπεράσει τις 1000 επαναλήψεις...
        criterion = f"Η αναζήτηση απέτυχε: μέγιστες επαναλήψεις ({MAX_TRIES})." # ...ενημερώνει τον χρήστη για τον λόγο που ο αλγόριθμος απέτυχε να βρει το βέλτιστο
        return x0, y0, None, criterion, False, x_path, y_path, z_path, tries # Επιστροφή των συγκεκριμένων σημείων, παραμέτρων, κριτηρίου και αριθμού επαναλήψεων

    # Αν η εκτέλεση επιτευχθεί, τότε επιστρέφονται τα εξής:
    # Οι τελικές τιμές των παραμέτρων, η τελική τιμή της συνάρτησης, ένα μήνυμα επιτυχίας & η κατάσταση επιτυχίας (True), η πορεία των τιμών x, y, f(x,y) και το συνολικό πλήθος επαναλήψεων
    return x0, y0, f_num(x0, y0), criterion, True, x_path, y_path, z_path, tries

# Χρήση της κύριας συνάρτησης main(), η οποία εκτελεί όλο το πρόγραμμα. Είναι υπέυθυνη για την εκτέλεση του βασικού προγράμματος
def main(): # Η συνάρτηση main()
    x0, y0 = Initial_Point() # Ζητά από τον χρήστη τα αρχικά σημεία (x0, y0), καλώντας την συνάρτηση Initial_Point()
    a, c1, c2, c3 = Parameters() # Ζητά από τον χρήστη τον ρυθμό εκμάθησης και τις σταθερές τερματισμού κριτηρίων (a, c1, c2, c3) καλώντας την συνάρτηση Parameters()

    f_sym = f() # Καλεί την συνάρτηση f(), η οποία ορίζει την συμβολική συνάρτηση που θέλουμε να βελτιστοποιήσουμε
    x, y = sp.symbols('x y') # Δημιουργεί τις συμβολικές μεταβλητές x, y με την βιβλιοθήκη Sympy

    # Μετατροπή της συνάρτησης από συμβολική σε αριθμητική συνάρτηση που μπορεί να υπολογίζει τις τιμές των x, y
    f_num = sp.lambdify((x, y), f_sym, "numpy")

    derivative_x_sym = sp.diff(f_sym, x) # Υπολογισμός μερικής παραγώγου της συνάρτησης f(x,y) ως προς x χρησιμοποιώντας την Sympy
    derivative_y_sym = sp.diff(f_sym, y) # Υπολογισμός μερικής παραγώγου της συνάρτησης f(x,y) ως προς y χρησιμοποιώντας την Sympy

    # Αποθήκευση αποτελεσμάτων μετά την εκτέλεση του κώδικα
    min_x, min_y, min_value, criterion, show_plots, x_path, y_path, z_path, total_tries = steepest_descent(f_num, x0, y0, a, c1, c2, c3, derivative_x_sym, derivative_y_sym)

    # Στην περίπτωση που ο μέγιστος αριθμός επαναλήψεων ξεπεραστεί, τότε δεν εμφανίζονται τα γραφήματα
    if not show_plots:
        print("Ο μέγιστος αριθμός επαναλήψεων ξεπεράστηκε.") # Εμφανίζεται το συγκεκριμένο μήνυμα ενημερώνοντας τον χρήστη
        return

    # Ο αλγόριθμος θα διαβάσει τις παρακάτω εντολές, σε περίπτωση που έχω:
    print("-------------------------------------------------------------------------------------")
    print(f"Ελάχιστο σημείο: ({min_x}, {min_y}), με τιμή συνάρτησης f(x, y) = {min_value}") # 1) τις τιμές του ελάχιστου σημείου, 2) της τιμής της συνάρτησης,
    print("Κριτήριο σύγκλισης ->", criterion) # 3) το κριτήριο που ικανοποιήθηκε
    print(f"Αριθμός επαναλήψεων: {total_tries}") # 4) τον αριθμό των επαναλήψεων

    # Αν τα παραπάνω αποτελέσματα είναι έγκυρα, τότε δημιουργούνται 3D και 2D γραφήματα τα οποία απεικονίζουν την πορεία του αλγορίθμου
    x_vals = np.linspace(-1.5, 1.5, 400) # Αφορά τις 400 ενδιάμεσες τιμές από -1.5 έως 1.5 για τον άξονα x
    y_vals = np.linspace(-1.5, 1.5, 400) # Αφορά τις 400 ενδιαμεσες τιμές από -1.5 έως 1.5 για τον άξονα y
    X, Y = np.meshgrid(x_vals, y_vals) # Δημιουργία πινάκων X (περιέχει όλες τις συντεταγμένες του άξονα x) και Y (περιέχει όλες τις συντεταγμένες του άξονα y)
    Z = f_num(X, Y) # Υπολογίζεται η τιμή της συνάρτησης f_num για κάθε ζεύγος (X,Y). Άρα, το Z αντιπροσωπεύει το ύψος του γραφήματος
    fig = plt.figure(figsize=(14, 6)) # Δημιουργία σχήματος με διαστάσεις: 14 ίντσες πλάτος και 6 ίντσες ύψος
    # figsize: Μέγεθος παραθύρου ώστε το γράφημα να είναι μεγάλο

    # 3D Plot (3 διαστάσεις: X, Y, Z)
    ax1 = fig.add_subplot(121, projection='3d')
    # Δημιουργία ενός υπογράφου στον πρώτο χώρο με διάταξη 1x2 (μία γραμμή και δύο στήλες), ο οποίος να έχει τρισδιάστατη μορφή (projection='3d')

    ax1.plot_surface(X, Y, Z, alpha=0.3, cmap='viridis') # Δημιουργία επιφάνειας
    # alpha=0.3: Δημιουργία ημιδιαφανούς επιφάνειας ώστε να διακρίνονται τα στοιχεία από κάτω
    # cmap='viridis': Αφορά τα χρώματα που θα απεικονίσουν την επιφάνεια (στυλ "viridis")

    ax1.plot(x_path, y_path, z_path, 'r-', label='Steepest Descent Path') # Η συνάρτηση αυτή σχεδιάζει την πορεία του αλγορίθμου της Steepest Descent
    # x_path, y_path, z_path: Λίστες που περιέχουν τις συντεταγμένες της πορείας του αλγορίθμου
    # r-: Ορίζει το χρώμα και τον τύπο της γραμμής (r: κόκκινο, -: συνεχής)
    # label='Steepest Descent Path': Ορίζει την ετικέτα

    ax1.scatter(min_x, min_y, min_value, color='red', s=100, label='Ελάχιστο Σημείο') # Τοποθέτηση του ελαχίστου
    # min_x, min_y, min_value: Περιέχουν τις συντεταγμένες του ελαχίστου
    # color='red': Ορίζει το χρώμα του ελαχίστου
    # s=100: Μέγεθος ελαχίστου (κουκίδας)
    # label='Ελάχιστο Σημείο': Ορίζει την ετικέτα

    # Ορίζει τις ετικέτες για τους άξονες x, y, z
    ax1.set_xlabel('$x$')
    ax1.set_ylabel('$y$'),
    ax1.set_zlabel('$f(x, y)$')

    # Προσθήκη λεζάντας για την εμφάνιση των labels που έχουμε καθορίσει για κάθε στοιχείο
    ax1.legend()


    # 2D Contour Plot (Ισοϋψεις Καμπύλες)
    ax2 = fig.add_subplot(122)
    # Δημιουργία ενός νέου υπογράφου στον δεύτερο χώρο με διάταξη 1x2 (μία γραμμή και δύο στήλες)

    ax2.contour(X, Y, Z, levels=50, cmap='viridis') # Σχεδίαση ισοϋψών καμπυλών
    # levels=50: Ορίζει τον αριθμό των ισοϋψών καμπυλών που θα σχεδιαστούν
    # cmap='viridis': Αφορά τα χρώματα που θα απεικονίσουν τις καμπύλες (στυλ "viridis")

    ax2.plot(x_path, y_path, 'r-', label='Steepest Descent Path') # Η συνάρτηση αυτή σχεδιάζει την πορεία του αλγορίθμου της Steepest Descent
    # x_path, y_path: Λίστες που περιέχουν τις συντεταγμένες της πορείας του αλγορίθμου
    # r-: Ορίζει το χρώμα και τον τύπο της γραμμής (r: κόκκινο, -: συνεχής)
    # label='Steepest Descent Path': Ορίζει την ετικέτα

    ax2.scatter(min_x, min_y, color='red', s=100, label='Ελάχιστο Σημείο') # Τοποθέτηση του ελαχίστου
    # min_x, min_y: Περιέχουν τις συντεταγμένες του ελαχίστου
    # color='red': Ορίζει το χρώμα του ελαχίστου
    # s=100: Μέγεθος ελαχίστου (κουκίδας)
    # label='Ελάχιστο Σημείο': Ορίζει την ετικέτα

    # Ορίζει τις ετικέτες για τους άξονες x, y
    ax2.set_xlabel('$x$')
    ax2.set_ylabel('$y$')

    # Προσθήκη λεζάντας για την εμφάνιση των labels που έχουμε καθορίσει για κάθε στοιχείο
    ax2.legend()

    # Εμφάνιση 3D και 2D γραφημάτων
    plt.show()

# Ολοκλήρωση της main
main()