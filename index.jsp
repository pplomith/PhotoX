<%@ page contentType="text/html;charset=UTF-8" language="java" %>

<html>
<head>
    <link href = "style_registration.css"
          rel = "stylesheet" type = "text/css" >
    <link href = "https://fonts.gstatic.com" rel="preconnect" >
    <link href = "https://fonts.googleapis.com/css2?family=Anaheim&display=swap" rel="stylesheet"> <script src="https://cdn.freecodecamp.org/testable-projects-fcc/v1/bundle.js"></script>
    <meta charset="UTF-8">
    <title>PhotoX</title>

</head>

<body>
    <div id = "outside">

        <form action="registration" id = "reg" method="post">

            <h1 id="title">Registration</h1>
            <p id="description">Compilare i campi per la registrazione e rispondere al questionario.</p>

            <fieldset>
                <legend>Registration</legend>
                <div>
                    <label id="name-label" for="name">Username:</label>
                    <input type="text" id="name" name="username" required></div>
                <div>
                    <label for="password">Password:</label>
                    <input type="text" name="password" id="password" required></div>
            </fieldset>

            <fieldset>
                <legend>Sezione 1</legend>

                <div>

                    <label for="1_1_1">Sei una persona che rispetta l'autorità</label>
                    <p>
                     <input type="radio" id="1_1_1" name="1_1" value="1">1<br>
                     <input type="radio" id="1_1_2" name="1_1" value="2">2<br>
                     <input type="radio" id="1_1_3" name="1_1" value="3">3<br>
                     <input type="radio" id="1_1_4" name="1_1" value="4">4<br>
                    </p>

                </div>

                <div>
                    <label for="1_2_1">Sei una persona solitamente entusiasta</label>
                    <p>
                        <input type="radio" id="1_2_1" name="1_2" value="1"> 1<br>
                        <input type="radio" id="1_2_2" name="1_2" value="2"> 2<br>
                        <input type="radio" id="1_2_3" name="1_2" value="3"> 3<br>
                        <input type="radio" id="1_2_4" name="1_2" value="4"> 4<br>
                    </p>

                </div>

                <div>

                    <label for="1_3_1">Sei una persona sensibile</label>
                    <p>
                        <input type="radio" id="1_3_1" name="1_3" value="1"> 1<br>
                        <input type="radio" id="1_3_2" name="1_3" value="2"> 2<br>
                        <input type="radio" id="1_3_3" name="1_3" value="3"> 3<br>
                        <input type="radio" id="1_3_4" name="1_3" value="4"> 4<br>
                    </p>

                </div>

                <div>

                    <label for="1_4_1">Sei una persona che apprezza ricevere istruzioni</label>
                    <p>
                        <input type="radio" id="1_4_1" name="1_4" value="1"> 1<br>
                        <input type="radio" id="1_4_2" name="1_4" value="2"> 2<br>
                        <input type="radio" id="1_4_3" name="1_4" value="3"> 3<br>
                        <input type="radio" id="1_4_4" name="1_4" value="4"> 4<br>
                    </p>

                </div>

            </fieldset>

            <fieldset>
                <legend>Sezione 2</legend>

                <div>

                    <label for="2_1_1">Sei una persona che prende l'iniziativa </label>
                    <p>
                    <input type="radio" id="2_1_1" name="2_1" value="1"> 1<br>
                    <input type="radio" id="2_1_2" name="2_1" value="2"> 2<br>
                    <input type="radio" id="2_1_3" name="2_1" value="3"> 3<br>
                    <input type="radio" id="2_1_4" name="2_1" value="4"> 4<br>
                    </p>
                </div>

                <div>
                    <label for="2_2_1">Sei una persona che ama assumersi dei rischi</label>
                    <p>
                    <input type="radio" id="2_2_1" name="2_2" value="1"> 1<br>
                    <input type="radio" id="2_2_2" name="2_2" value="2"> 2<br>
                    <input type="radio" id="2_2_3" name="2_2" value="3"> 3<br>
                    <input type="radio" id="2_2_4" name="2_2" value="4"> 4<br>
                    </p>
                </div>

                <div>
                    <label for="2_3_1">Sei una persona leale</label>
                    <p>
                    <input type="radio" id="2_3_1" name="2_3" value="1"> 1<br>
                    <input type="radio" id="2_3_2" name="2_3" value="2"> 2<br>
                    <input type="radio" id="2_3_3" name="2_3" value="3"> 3<br>
                    <input type="radio" id="2_3_4" name="2_3" value="4"> 4<br>
                    </p>
                </div>

                <div>

                    <label for="2_4_1">Sei una persona accurata</label>
                    <p>
                    <input type="radio" id="2_4_1" name="2_4" value="1"> 1<br>
                    <input type="radio" id="2_4_2" name="2_4" value="2"> 2<br>
                    <input type="radio" id="2_4_3" name="2_4" value="3"> 3<br>
                    <input type="radio" id="2_4_4" name="2_4" value="4"> 4<br>
                    </p>
                </div>

            </fieldset>



            <fieldset>
                <legend>Sezione 3</legend>

                <div>

                    <label for="3_1_1">Sei una persona determinata</label>
                    <p>
                    <input type="radio" id="3_1_1" name="3_1" value="1"> 1<br>
                    <input type="radio" id="3_1_2" name="3_1" value="2"> 2<br>
                    <input type="radio" id="3_1_3" name="3_1" value="3"> 3<br>
                    <input type="radio" id="3_1_4" name="3_1" value="4"> 4<br>
                    </p>
                </div>

                <div>
                    <label for="3_2_1">Sei un visionario</label>
                    <p>
                    <input type="radio" id="3_2_1" name="3_2" value="1"> 1<br>
                    <input type="radio" id="3_2_2" name="3_2" value="2"> 2<br>
                    <input type="radio" id="3_2_3" name="3_2" value="3"> 3<br>
                    <input type="radio" id="3_2_4" name="3_2" value="4"> 4<br>
                    </p>
                </div>

                <div>
                    <label for="3_3_1">Sei una persona calma </label>
                    <p>
                    <input type="radio" id="3_3_1" name="3_3" value="1"> 1<br>
                    <input type="radio" id="3_3_2" name="3_3" value="2"> 2<br>
                    <input type="radio" id="3_3_3" name="3_3" value="3"> 3<br>
                    <input type="radio" id="3_3_4" name="3_3" value="4"> 4<br>
                    </p>
                </div>

                <div>

                    <label for="3_4_1">Sei una persona concreta</label>
                    <p>
                    <input type="radio" id="3_4_1" name="3_4" value="1"> 1<br>
                    <input type="radio" id="3_4_2" name="3_4" value="2"> 2<br>
                    <input type="radio" id="3_4_3" name="3_4" value="3"> 3<br>
                    <input type="radio" id="3_4_4" name="3_4" value="4"> 4<br>
                    </p>
                </div>

            </fieldset>


            <fieldset>
                <legend>Sezione 4</legend>

                <div>

                    <label for="4_1_1">Sei una persona intraprendente</label>
                    <p>
                    <input type="radio" id="4_1_1" name="4_1" value="1"> 1<br>
                    <input type="radio" id="4_1_2" name="4_1" value="2"> 2<br>
                    <input type="radio" id="4_1_3" name="4_1" value="3"> 3<br>
                    <input type="radio" id="4_1_4" name="4_1" value="4"> 4<br>
                    </p>
                </div>

                <div>
                    <label for="4_2_1"> Sei una persona che adora esprimere i propri pensieri attraverso il linguaggio </label>
                    <p>
                    <input type="radio" id="4_2_1" name="4_2" value="1"> 1<br>
                    <input type="radio" id="4_2_2" name="4_2" value="2"> 2<br>
                    <input type="radio" id="4_2_3" name="4_2" value="3"> 3<br>
                    <input type="radio" id="4_2_4" name="4_2" value="4"> 4<br>
                    </p>
                </div>

                <div>
                    <label for="4_3_1">Sei una persona che apprezza la routine</label>
                    <p>
                    <input type="radio" id="4_3_1" name="4_3" value="1"> 1<br>
                    <input type="radio" id="4_3_2" name="4_3" value="2"> 2<br>
                    <input type="radio" id="4_3_3" name="4_3" value="3"> 3<br>
                    <input type="radio" id="4_3_4" name="4_3" value="4"> 4<br>
                    </p>
                </div>

                <div>

                    <label for="4_4_1">Sei una persona prevedibile</label>
                    <p>
                    <input type="radio" id="4_4_1" name="4_4" value="1"> 1<br>
                    <input type="radio" id="4_4_2" name="4_4" value="2"> 2<br>
                    <input type="radio" id="4_4_3" name="4_4" value="3"> 3<br>
                    <input type="radio" id="4_4_4" name="4_4" value="4"> 4<br>
                    </p>
                </div>

            </fieldset>


            <fieldset>
                <legend>Sezione 5</legend>

                <div>

                    <label for="5_1_1">Sei una persona competitiva</label>
                    <p>
                    <input type="radio" id="5_1_1" name="5_1" value="1"> 1<br>
                    <input type="radio" id="5_1_2" name="5_1" value="2"> 2<br>
                    <input type="radio" id="5_1_3" name="5_1" value="3"> 3<br>
                    <input type="radio" id="5_1_4" name="5_1" value="4"> 4<br>
                    </p>
                </div>

                <div>
                    <label for="5_2_1">Sei una persona che ama promuoversi</label>
                    <p>
                    <input type="radio" id="5_2_1" name="5_2" value="1"> 1<br>
                    <input type="radio" id="5_2_2" name="5_2" value="2"> 2<br>
                    <input type="radio" id="5_2_3" name="5_2" value="3"> 3<br>
                    <input type="radio" id="5_2_4" name="5_2" value="4"> 4<br>
                    </p>
                </div>

                <div>
                    <label for="5_3_1">Sei una persona che non apprezza il cambiamento</label>
                    <p>
                    <input type="radio" id="5_3_1" name="5_3" value="1"> 1<br>
                    <input type="radio" id="5_3_2" name="5_3" value="2"> 2<br>
                    <input type="radio" id="5_3_3" name="5_3" value="3"> 3<br>
                    <input type="radio" id="5_3_4" name="5_3" value="4"> 4<br>
                    </p>
                </div>

                <div>

                    <label for="5_4_1">Sei una persona pratica </label>
                    <p>
                    <input type="radio" id="5_4_1" name="5_4" value="1"> 1<br>
                    <input type="radio" id="5_4_2" name="5_4" value="2"> 2<br>
                    <input type="radio" id="5_4_3" name="5_4" value="3"> 3<br>
                    <input type="radio" id="5_4_4" name="5_4" value="4"> 4<br>
                    </p>
                </div>

            </fieldset>

            <fieldset>
                <legend>Sezione 6</legend>

                <div>

                    <label for="6_1_1">Sei una persona che ama il problem solving</label>
                    <p>
                    <input type="radio" id="6_1_1" name="6_1" value="1"> 1<br>
                    <input type="radio" id="6_1_2" name="6_1" value="2"> 2<br>
                    <input type="radio" id="6_1_3" name="6_1" value="3"> 3<br>
                    <input type="radio" id="6_1_4" name="6_1" value="4"> 4<br>
                    </p>
                </div>

                <div>
                    <label for="6_2_1">Sei una persona che apprezza essere popolare</label>
                    <p>
                    <input type="radio" id="6_2_1" name="6_2" value="1"> 1<br>
                    <input type="radio" id="6_2_2" name="6_2" value="2"> 2<br>
                    <input type="radio" id="6_2_3" name="6_2" value="3"> 3<br>
                    <input type="radio" id="6_2_4" name="6_2" value="4"> 4<br>
                    </p>
                </div>

                <div>
                    <label for="6_3_1">Sei una persona che ama donare agli altri</label>
                    <p>
                    <input type="radio" id="6_3_1" name="6_3" value="1"> 1<br>
                    <input type="radio" id="6_3_2" name="6_3" value="2"> 2<br>
                    <input type="radio" id="6_3_3" name="6_3" value="3"> 3<br>
                    <input type="radio" id="6_3_4" name="6_3" value="4"> 4<br>
                    </p>
                </div>

                <div>
                    <label for="6_4_1">Sei una persona che limita i suoi ragionamenti ai fatti e al reale</label>
                    <p>
                    <input type="radio" id="6_4_1" name="6_4" value="1"> 1<br>
                    <input type="radio" id="6_4_2" name="6_4" value="2"> 2<br>
                    <input type="radio" id="6_4_3" name="6_4" value="3"> 3<br>
                    <input type="radio" id="6_4_4" name="6_4" value="4"> 4<br>
                    </p>
                </div>

            </fieldset>


            <fieldset>
                <legend>Sezione 7</legend>

                <div>

                    <label for="7_1_1">Sei una persona produttiva</label>
                    <p>
                    <input type="radio" id="7_1_1" name="7_1" value="1"> 1<br>
                    <input type="radio" id="7_1_2" name="7_1" value="2"> 2<br>
                    <input type="radio" id="7_1_3" name="7_1" value="3"> 3<br>
                    <input type="radio" id="7_1_4" name="7_1" value="4"> 4<br>
                    </p>
                </div>

                <div>
                    <label for="7_2_1">Sei una persona che adora il divertimento</label>
                    <p>
                    <input type="radio" id="7_2_1" name="7_2" value="1"> 1<br>
                    <input type="radio" id="7_2_2" name="7_2" value="2"> 2<br>
                    <input type="radio" id="7_2_3" name="7_2" value="3"> 3<br>
                    <input type="radio" id="7_2_4" name="7_2" value="4"> 4<br>
                    </p>
                </div>

                <div>
                    <label for="7_3_1">Sei una persona che evita il confronto</label>
                    <p>
                    <input type="radio" id="7_3_1" name="7_3" value="1"> 1<br>
                    <input type="radio" id="7_3_2" name="7_3" value="2"> 2<br>
                    <input type="radio" id="7_3_3" name="7_3" value="3"> 3<br>
                    <input type="radio" id="7_3_4" name="7_3" value="4"> 4<br>
                    </p>
                </div>

                <div>
                    <label for="7_4_1">Sei una persona coscienziosa</label>
                    <p>
                    <input type="radio" id="7_4_1" name="7_4" value="1"> 1<br>
                    <input type="radio" id="7_4_2" name="7_4" value="2"> 2<br>
                    <input type="radio" id="7_4_3" name="7_4" value="3"> 3<br>
                    <input type="radio" id="7_4_4" name="7_4" value="4"> 4<br>
                    </p>
                </div>

            </fieldset>


            <fieldset>
                <legend>Sezione 8</legend>

                <div>

                    <label for="8_1_1">Sei una persona di spessore e con un carattere deciso</label>
                    <p>
                    <input type="radio" id="8_1_1" name="8_1" value="1"> 1<br>
                    <input type="radio" id="8_1_2" name="8_1" value="2"> 2<br>
                    <input type="radio" id="8_1_3" name="8_1" value="3"> 3<br>
                    <input type="radio" id="8_1_4" name="8_1" value="4"> 4<br>
                    </p>
                </div>

                <div>
                    <label for="8_2_1">Sei una persona che apprezza la varietà</label>
                    <p>
                    <input type="radio" id="8_2_1" name="8_2" value="1"> 1<br>
                    <input type="radio" id="8_2_2" name="8_2" value="2"> 2<br>
                    <input type="radio" id="8_2_3" name="8_2" value="3"> 3<br>
                    <input type="radio" id="8_2_4" name="8_2" value="4"> 4<br>
                    </p>
                </div>

                <div>
                    <label for="8_3_1">Sei una persona empatica</label>
                    <p>
                    <input type="radio" id="8_3_1" name="8_3" value="1"> 1<br>
                    <input type="radio" id="8_3_2" name="8_3" value="2"> 2<br>
                    <input type="radio" id="8_3_3" name="8_3" value="3"> 3<br>
                    <input type="radio" id="8_3_4" name="8_3" value="4"> 4<br>
                    </p>
                </div>

                <div>
                    <label for="8_4_1">Sei un perfezionista</label>
                    <p>
                    <input type="radio" id="8_4_1" name="8_4" value="1"> 1<br>
                    <input type="radio" id="8_4_2" name="8_4" value="2"> 2<br>
                    <input type="radio" id="8_4_3" name="8_4" value="3"> 3<br>
                    <input type="radio" id="8_4_4" name="8_4" value="4"> 4<br>
                    </p>
                </div>

            </fieldset>

            <fieldset>
                <legend>Sezione 9</legend>

                <div>

                    <label for="9_1_1">Sei una persona che adora prendere decisioni</label>
                    <p>
                    <input type="radio" id="9_1_1" name="9_1" value="1"> 1<br>
                    <input type="radio" id="9_1_2" name="9_1" value="2"> 2<br>
                    <input type="radio" id="9_1_3" name="9_1" value="3"> 3<br>
                    <input type="radio" id="9_1_4" name="9_1" value="4"> 4<br>
                    </p>
                </div>

                <div>
                    <label for="9_2_1">Sei una persona spontanea</label>
                    <p>
                    <input type="radio" id="9_2_1" name="9_2" value="1"> 1<br>
                    <input type="radio" id="9_2_2" name="9_2" value="2"> 2<br>
                    <input type="radio" id="9_2_3" name="9_2" value="3"> 3<br>
                    <input type="radio" id="9_2_4" name="9_2" value="4"> 4<br>
                    </p>
                </div>

                <div>
                    <label for="9_3_1">Sei una persona che ama influenzare l'ambiente circostante</label>
                    <p>
                    <input type="radio" id="9_3_1" name="9_3" value="1"> 1<br>
                    <input type="radio" id="9_3_2" name="9_3" value="2"> 2<br>
                    <input type="radio" id="9_3_3" name="9_3" value="3"> 3<br>
                    <input type="radio" id="9_3_4" name="9_3" value="4"> 4<br>
                    </p>
                </div>

                <div>
                    <label for="9_4_1">Sei una persona che cura molto i dettagli</label>
                    <p>
                    <input type="radio" id="9_4_1" name="9_4" value="1"> 1<br>
                    <input type="radio" id="9_4_2" name="9_4" value="2"> 2<br>
                    <input type="radio" id="9_4_3" name="9_4" value="3"> 3<br>
                    <input type="radio" id="9_4_4" name="9_4" value="4"> 4<br>
                    </p>
                </div>

            </fieldset>

            <fieldset>
                <legend>Sezione 10</legend>

                <div>

                    <label for="10_1_1">Sei una persona insistente</label>
                    <p>
                    <input type="radio" id="10_1_1" name="10_1" value="1"> 1<br>
                    <input type="radio" id="10_1_2" name="10_1" value="2"> 2<br>
                    <input type="radio" id="10_1_3" name="10_1" value="3"> 3<br>
                    <input type="radio" id="10_1_4" name="10_1" value="4"> 4<br>
                    </p>
                </div>
                <div>
                    <label for="10_2_1">Sei una persona che apprezza ispirare gli altri</label>
                    <p>
                    <input type="radio" id="10_2_1" name="10_2" value="1"> 1<br>
                    <input type="radio" id="10_2_2" name="10_2" value="2"> 2<br>
                    <input type="radio" id="10_2_3" name="10_2" value="3"> 3<br>
                    <input type="radio" id="10_2_4" name="10_2" value="4"> 4<br>
                    </p>
                </div>

                <div>
                    <label for="10_3_1">Sei una persona pacificatrice</label>
                    <p>
                    <input type="radio" id="10_3_1" name="10_3" value="1"> 1<br>
                    <input type="radio" id="10_3_2" name="10_3" value="2"> 2<br>
                    <input type="radio" id="10_3_3" name="10_3" value="3"> 3<br>
                    <input type="radio" id="10_3_4" name="10_3" value="4"> 4<br>
                    </p>
                </div>

                <div>
                    <label for="10_4_1">Sei una persona con una mente analitica</label>
                    <p>
                    <input type="radio" id="10_4_1" name="10_4" value="1"> 1<br>
                    <input type="radio" id="10_4_2" name="10_4" value="2"> 2<br>
                    <input type="radio" id="10_4_3" name="10_4" value="3"> 3<br>
                    <input type="radio" id="10_4_4" name="10_4" value="4"> 4<br>
                    </p>
                </div>

            </fieldset>

            <div id="submitbutton">
                <button type="submit"> Complete Registration </button> </div>

        </form>
    </div>
</body>
</html>