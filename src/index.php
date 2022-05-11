<?php

$project = $_ENV["PROJECT"];
$site_name = $_ENV["SITE_NAME"];
$host = $_ENV["HOST"];

?>

<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="">
  <title>Bridgehead Overview</title>
  <!-- Bootstrap core CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
    crossorigin="anonymous"></script>
</head>

<body class="d-flex flex-column min-vh-100">

  <nav class="navbar navbar-light" style="background-color: #aad7f6;">
    <h2 class="pb-2 border-bottom">Bridgehead in <?php print $site_name; ?></h2>
  </nav>
  <div class="container px-4 py-5" id="featured-3">
    <div>
      <h2>Components</h2>
      <h3>Central</h3>
      <table class="table">
        <thead class="thead-dark">
          <tr>
            <th style="width: 50%">Group</th>
            <th style="width: 50%">Service</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>CCP-IT</td>
            <td><a href="https://monitor.vmitro.de/icingaweb2/dashboard">Monitoring Service</td>
          </tr>
<?php

require("central-$project.php");

?>
        </tbody>
      </table>
    </div>

    <div>
      <h3>Local</h3>
      <table class="table">
        <thead class="thead-dark">
          <tr>
            <th style="width: 50%">Project</th>
            <th style="width: 50%">Services</th>
          </tr>
        </thead>
        <tbody>
<?php
require("local-$project.php");
?>
        </tbody>
      </table>
    </div>
    <footer class="footer mt-auto py-3">
     <img src="<?php echo $project; ?>.svg" style="max-width: 30%; height: auto;"><span style="float: right;"><a href="https://github.com/samply/bridgehead"><button type="button" class="btn btn-primary">Documentation</button></a></span>
    </footer>
</body>

</html>
