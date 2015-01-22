Title: Contact
sortorder: 99

<h3><i class="fa fa-map-marker"></i>-title-</h3>
<p>UNIVERSIDAD DE LA LAGUNA<br>
-resto de la dirección-</p>

<h3><i class="fa fa-envelope"></i> Contact Us</h3>
<noscript><p>For further information, please don't hesitate to contact us by e-mail to <a href="mailto:direccion_de_contacto"><i class="fa fa-envelope"></i>verdino@ull.es</a>.</p></noscript>
<p class="jsonly">For further information, you can leave a message using the contact form below.</p>
<div class="container-fluid jsonly">
    <div class="row">
        <div class="col-md-12">
            <div class="section">
                <ul class="nav nav-tabs header">
                    <li class="active">Contact form</li>
                </ul>
                <div class="content">
                    <div id="form-messages" role="alert"></div>
                    <form id="contact-form" method="post" action="php/mailer.php">
                        <div class="form-group" style="display: none">
                            <input type="text" class="form-control" id="honeypot" name="honeypot">
                        </div>
                        <div class="form-group">
                            <label class="">Your name: </label>
                            <input type="text" class="form-control" id="name" name="name" required>
                        </div>
                        <div class="form-group">
                            <label class="">Your e-mail address: </label>
                            <input type="email" class="form-control" id="email" name="email" required>
                        </div>
                        <div class="form-group">
                            <label class="">Message: </label>
                            <textarea class="form-control" rows="5" id="message" name="message" required></textarea>
                        </div>
                        <div class="checkbox">
                            <label>
                                <input type="checkbox" id="sendcopy" name="sendcopy" value="sendcopy"> Send yourself a copy
                            </label>
                        </div>
                        <button type="submit" class="btn btn-primary">Send</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
