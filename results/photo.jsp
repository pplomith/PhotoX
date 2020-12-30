<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<%@ page import="java.util.ArrayList" %>

<!DOCTYPE html>
<head>
    <title>Homepage</title>
    <link href = "style_imagepage.css" rel = "stylesheet" type = "text/css" >
    <link href = "https://upload.wikimedia.org/wikipedia/commons/d/db/CMYK-color_model.png"
          rel = "icon" type = "image/png"/>
</head>
<body>
<% ArrayList<String> foto = (ArrayList<String>) request.getAttribute("foto");%>

<%@include file="navbar.jsp" %>

<div class="content">
    <div id="masonry" class="masonry">


        <%for (int i = 0; i < foto.size(); i++) {%>
        <div class="item">
            <form action="" method="get">
                <img src="<%=foto.get(i)%>">
            </form>
        </div>
        <%}%>

    </div>
</div>
</body>

</html>
