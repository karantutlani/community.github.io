start = """
  <head>
    <title>Community Project</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
    <link rel="stylesheet" href="assets/css/main.css" />
  <style>
  ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color: #333;
  }
  
  li {
    float: left;
  }
  
  li a, .dropbtn {
    display: inline-block;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
  }
  
  li a:hover, .dropdown:hover .dropbtn {
    background-color: red;
  }
  
  li.dropdown {
    display: inline-block;
  }
  
  .dropdown-content {
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
  }
  
  .dropdown-content a {
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
    text-align: left;
  }
  
  .dropdown-content a:hover {background-color: #f1f1f1;}
  
  .dropdown:hover .dropdown-content {
    display: block;
  }
  </style>
  </head>

"""

header = """
<body>
  <ul>
    <li><a href="index.html">Home</a></li>
    <li class="dropdown">
      <a href="javascript:void(0)" class="dropbtn">Data</a>
      <div class="dropdown-content">
        <a href="Abuse.html">Abuse</a>
        <a href="Addictions.html">Addictions</a>
        <a href="AIDS Hepatitis C.html">AIDS Hepatitis C</a>
        <a href="Anger Management.html">Anger Management</a>
        <a href="Bereavement.html">Bereavement</a>
        <a href="Black Lives.html">Black Lives</a>
        <a href="Brain InjuryTumour.html">Brain InjuryTumour</a>
        <a href="Clothing Donations.html">Clothing Donations</a>
        <a href="Community Programs.html">Community Programs</a>
        <a href="Disability.html">Disability</a>
        <a href="Education.html">Education</a>
        <a href="Emergency Services.html">Emergency Services</a>
        <a href="Employment Services.html">Employment Services</a>
        <a href="Family Services.html">Family Services</a>
        <a href="Financial.html">Financial</a>
        <a href="Food Banks.html">Food Banks</a>
        <a href="Francophones.html">Francophones</a>
        <a href="Government.html">Government</a>
        <a href="Healthcare.html">Healthcare</a>
        <a href="Homelessness.html">Homelessness</a>
        <a href="Housing.html">Housing</a>
        <a href="Indigenous People.html">Indigenous People</a>
        <a href="Legal Assistance.html">Legal Assistance</a>
        <a href="LGBTQ2S+.html">LGBTQ2S+</a>
        <a href="Mental Health.html">Mental Health</a>
        <a href="Newcomers.html">Newcomers</a>
        <a href="Older Adults.html">Older Adults</a>
        <a href="Pregnancy.html">Pregnancy</a>
        <a href="Transportation.html">Transportation</a>
        <a href="Youth.html">Youth</a>
      </div>
    </li>
  </ul>
"""
def banner(banner_name):
	banner = f"""
				<!-- Banner -->
				<div id="banner-wrapper">
					<div class="container">

						<div id="banner">
							<h2>{banner_name}</h2>
							
						</div>

					</div>
				</div>
	"""
	return banner
# <span>And put something almost as cool here, but a bit longer ...</span>

filter= """

<input type="text" id="myInput" onkeyup="searchTable()" placeholder="Search for ...">

"""

main = """
		<!-- Main -->
			<div id="main">
				<div class="container">
					<div class="row main-row">
						<div class="col-4 col-12-medium">

							<section>
								<h2>Welcome to Minimaxing!</h2>
								<p>This is <strong>Minimaxing</strong>, a fully responsive HTML5 site template designed by <a href="http://twitter.com/ajlkn">AJ</a> and released for free by <a href="http://html5up.net">HTML5 UP</a>. It features
								a simple, lightweight design, solid HTML5 and CSS3 code, and full responsive support for desktop, tablet, and small displays.</p>
								<footer class="controls">
									<a href="http://html5up.net" class="button">More cool designs ...</a>
								</footer>
							</section>

						</div>
						<div class="col-4 col-6-medium col-12-small">

							<section>
								<h2>Who are you guys?</h2>
								<ul class="small-image-list">
									<li>
										<a href="#"><img src="images/pic2.jpg" alt="" class="left" /></a>
										<h4>Jane Anderson</h4>
										<p>Varius nibh. Suspendisse vitae magna eget et amet mollis justo facilisis amet quis.</p>
									</li>
									<li>
										<a href="#"><img src="images/pic1.jpg" alt="" class="left" /></a>
										<h4>James Doe</h4>
										<p>Vitae magna eget odio amet mollis justo facilisis amet quis. Sed sagittis consequat.</p>
									</li>
								</ul>
							</section>

						</div>
						<div class="col-4 col-6-medium col-12-small">

							<section>
								<h2>How about some links?</h2>
								<div>
									<div class="row">
										<div class="col-6 col-12-small">
											<ul class="link-list">
												<li><a href="#">Sed neque nisi consequat</a></li>
												<li><a href="#">Dapibus sed mattis blandit</a></li>
												<li><a href="#">Quis accumsan lorem</a></li>
												<li><a href="#">Suspendisse varius ipsum</a></li>
												<li><a href="#">Eget et amet consequat</a></li>
											</ul>
										</div>
										<div class="col-6 col-12-small">
											<ul class="link-list">
												<li><a href="#">Quis accumsan lorem</a></li>
												<li><a href="#">Sed neque nisi consequat</a></li>
												<li><a href="#">Eget et amet consequat</a></li>
												<li><a href="#">Dapibus sed mattis blandit</a></li>
												<li><a href="#">Vitae magna sed dolore</a></li>
											</ul>
										</div>
									</div>
								</div>
							</section>

						</div>
						<div class="col-6 col-12-medium">

							<section>
								<h2>An assortment of pictures and text</h2>
								<p>Duis neque nisi, dapibus sed mattis quis, rutrum et accumsan.
								Suspendisse nibh. Suspendisse vitae magna eget odio amet mollis
								justo facilisis quis. Sed sagittis mauris amet tellus gravida
								lorem ipsum dolor sit amet consequat blandit lorem ipsum dolor
								sit amet consequat sed dolore.</p>
								<ul class="big-image-list">
									<li>
										<a href="#"><img src="images/pic3.jpg" alt="" class="left" /></a>
										<h3>Magna Gravida Dolore</h3>
										<p>Varius nibh. Suspendisse vitae magna eget et amet mollis justo
										facilisis amet quis consectetur in, sollicitudin vitae justo. Cras
										Maecenas eu arcu purus, phasellus fermentum elit.</p>
									</li>
									<li>
										<a href="#"><img src="images/pic4.jpg" alt="" class="left" /></a>
										<h3>Magna Gravida Dolore</h3>
										<p>Varius nibh. Suspendisse vitae magna eget et amet mollis justo
										facilisis amet quis consectetur in, sollicitudin vitae justo. Cras
										Maecenas eu arcu purus, phasellus fermentum elit.</p>
									</li>
									<li>
										<a href="#"><img src="images/pic5.jpg" alt="" class="left" /></a>
										<h3>Magna Gravida Dolore</h3>
										<p>Varius nibh. Suspendisse vitae magna eget et amet mollis justo
										facilisis amet quis consectetur in, sollicitudin vitae justo. Cras
										Maecenas eu arcu purus, phasellus fermentum elit.</p>
									</li>
								</ul>
							</section>

						</div>
						<div class="col-6 col-12-medium">

							<article class="blog-post">
								<h2>Just another blog post</h2>
								<a class="comments" href="#">33 comments</a>
								<a href="#"><img src="images/pic6.jpg" alt="" class="top blog-post-image" /></a>
								<h3>Magna Gravida Dolore</h3>
								<p>Aenean non massa sapien. In hac habitasse platea dictumst.
								Maecenas sodales purus et nulla sodales aliquam. Aenean ac
								porttitor metus. In hac habitasse platea dictumst. Phasellus
								blandit turpis in leo scelerisque mollis. Nulla venenatis
								ipsum nec est porta rhoncus. Mauris sodales sed pharetra
								nisi nec consectetur. Cras elit magna, hendrerit nec
								consectetur in, sollicitudin vitae justo. Cras amet aliquet
								Aliquam ligula turpis, feugiat id fermentum malesuada,
								rutrum eget turpis. Mauris sodales sed pharetra nisi nec
								consectetur. Cras elit magna, hendrerit nec consectetur
								in sollicitudin vitae.</p>
								<footer class="controls">
									<a href="#" class="button">Continue Reading</a>
								</footer>
							</article>

						</div>
					</div>
				</div>
			</div>

"""

footer = """
			<!-- Footer -->
			<div id="footer-wrapper">
				<div class="container">
					<div class="row">
						<div class="col-8 col-12-medium">

							<section>
								<h2>How about a truckload of links?</h2>
								<div>
									<div class="row">
										<div class="col-3 col-6-medium col-12-small">
											<ul class="link-list">
												<li><a href="#">Sed neque nisi consequat</a></li>
												<li><a href="#">Dapibus sed mattis blandit</a></li>
												<li><a href="#">Quis accumsan lorem</a></li>
												<li><a href="#">Suspendisse varius ipsum</a></li>
												<li><a href="#">Eget et amet consequat</a></li>
											</ul>
										</div>
										<div class="col-3 col-6-medium col-12-small">
											<ul class="link-list">
												<li><a href="#">Quis accumsan lorem</a></li>
												<li><a href="#">Sed neque nisi consequat</a></li>
												<li><a href="#">Eget et amet consequat</a></li>
												<li><a href="#">Dapibus sed mattis blandit</a></li>
												<li><a href="#">Vitae magna sed dolore</a></li>
											</ul>
										</div>
										<div class="col-3 col-6-medium col-12-small">
											<ul class="link-list">
												<li><a href="#">Sed neque nisi consequat</a></li>
												<li><a href="#">Dapibus sed mattis blandit</a></li>
												<li><a href="#">Quis accumsan lorem</a></li>
												<li><a href="#">Suspendisse varius ipsum</a></li>
												<li><a href="#">Eget et amet consequat</a></li>
											</ul>
										</div>
										<div class="col-3 col-6-medium col-12-small">
											<ul class="link-list">
												<li><a href="#">Quis accumsan lorem</a></li>
												<li><a href="#">Sed neque nisi consequat</a></li>
												<li><a href="#">Eget et amet consequat</a></li>
												<li><a href="#">Dapibus sed mattis blandit</a></li>
												<li><a href="#">Vitae magna sed dolore</a></li>
											</ul>
										</div>
									</div>
								</div>
							</section>

						</div>
						<div class="col-4 col-12-medium">

							<section>
								<h2>Something of interest</h2>
								<p>Duis neque nisi, dapibus sed mattis quis, rutrum accumsan sed.
								Suspendisse eu varius nibh. Suspendisse vitae magna eget odio amet
								mollis justo facilisis quis. Sed sagittis mauris amet tellus gravida
								lorem ipsum dolor sit blandit.</p>
								<footer class="controls">
									<a href="#" class="button">Oh, please continue ....</a>
								</footer>
							</section>

						</div>
					</div>
					<div class="row">
						<div class="col-12">

							<div id="copyright">
								&copy; Untitled. All rights reserved. | Design: <a href="http://html5up.net">HTML5 UP</a>
							</div>

						</div>
					</div>
				</div>
			</div>

	</div>


"""

scripts = """
	<!-- Scripts -->
		<script src="assets/js/jquery.min.js"></script>
		<script src="assets/js/browser.min.js"></script>
		<script src="assets/js/breakpoints.min.js"></script>
		<script src="assets/js/util.js"></script>
		<script src="assets/js/main.js"></script>
		<script>
		function searchTable() {
			var input, filter, found, table, tr, td, i, j;
			input = document.getElementById("myInput");
			filter = input.value.toUpperCase();
			table = document.getElementById("myTable");
			tr = table.getElementsByTagName("tr");
			for (i = 0; i < tr.length; i++) {
				td = tr[i].getElementsByTagName("td");
				for (j = 0; j < td.length; j++) {
					if (td[j].innerHTML.toUpperCase().indexOf(filter) > -1) {
						found = true;
					}
				}
				if (found) {
					tr[i].style.display = "";
					found = false;
				} else {
					tr[i].style.display = "none";
				}
			}
		}
		</script>
</body>
</html>
"""
