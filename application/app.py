from flask import Flask, render_template

app = Flask(__name__,static_folder='static')

products = [
    {"id": 1, "name": "Airpods pro", "price": "$10.00", 
     "description": '''RICHER AUDIO EXPERIENCE — The Apple-designed H2 chip helps to create more intelligent noise cancellation and deeply immersive sound. 
                       The low-distortion, custom-built driver delivers crisp, clear high notes and full, rich bass in stunning definition.
                       NEXT-LEVEL ACTIVE NOISE CANCELLATION — Up to 2x more Active Noise Cancellation for dramatically less noise when you want to focus. 
                       Transparency mode lets you hear the world around you, and Adaptive Audio seamlessly blends Active Noise Cancellation and Transparency mode for the best listening experience in any environment.
                       CUSTOMIZABLE FIT — Includes four pairs of silicone tips (XS, S, M, L) to fit a wide range of ears and provide all-day comfort. 
                       The tips create an acoustic seal to help keep out noise and secure AirPods Pro in place.
                       DUST, SWEAT, AND WATER RESISTANT — Both AirPods Pro and the MagSafe Charging Case are IP54 dust, sweat, and water resistant, so you can listen comfortably in more conditions.''', "image":"images/airpods.jpg"},
    
    
    {"id": 2, "name": "Samsung 65-Inch QLED 4K TV", "price": "$20.00", 
     "description": ''' Meet the Echo Dot - Our most popular smart speaker with Alexa. The sleek, compact design delivers crisp vocals and balanced bass for full sound.
                        Voice control your entertainment - Stream songs from Amazon Music, Apple Music, Spotify, SiriusXM, and others. Play music, audiobooks, and podcasts throughout your home with multi-room music.
                        Ready to help - Ask Alexa to tell a joke, play music, answer questions, play the news, check the weather, set alarms, and more.
                        Control your smart home - Use your voice to turn on lights, adjust thermostats, and lock doors with compatible devices.
                        Start Routines with your motion - Turn on compatible lights, play your Flash Briefing, or turn on the coffee maker when you walk into the room.''', 'image':"images/samsung.jpg"},
    
    
    {"id": 3, "name": "Amazon Echo Dot (4th Gen)", "price": "$30.00", 
     "description": '''QUANTUM PROCESSOR 4K: Elevate your picture to 4K with machine based AI.
                       Image Aspect ratio:16:9.Controller type:Amazon AlexaMOTION XCELERATOR TURBO plus: Exceptional motion enhancements up to 4K 120Hz.
                       DUAL LED Backlight: Dedicated warm and cool LED backlights provide enhanced contrast.
                       100% COLOR VOLUME WITH QUANTUM DOT: A billion stay-true shades of breathtaking color. 
                       QLED televisions can produce 100% Color Volume in the DCI-P3 color space, the format for most cinema screens and HDR movies for television.
                       ALEXA BUILT-IN: Ask more from your TV. Just ask Alexa to open apps, change the channel, search for movies and shows, play music, control your smart home devices and more. 
                       To talk to Alexa, press and hold the mic button on your remote. If you have hands-free enabled just say, "Alexa" and ask a question.''',"image":"images/echodot.jpg"},
    
    
    
    {"id": 4, "name": "Nintendo Switch", "price": "$40.00", 
     "description": '''6.2” LCD screenThree play modes: TV, tabletop, and handheld 
                       Local co-op, online, and local wireless multiplayerDetachable Joy-Con controllersNintendo Switch is the home of Mario & friends''',"image":"static/nintendo.jpg"},
    
    
    {"id": 5, "name": "Fitbit Charge 4", "price": "$50.00", 
     "description": '''4in l x 0.9in w x 0.5in h, 
                       Backlit OLED display, 
                       GPS, 
                       Optical heart rate monitor - 24/7 heart rate tracking, 
                       NFC, 
                       3-axis accelerometerGet call and calendar alerts, send text notifications and quick replies. 
                       Automatic sleep tracking and silent alarms on your wristBattery life up to 7 days, or up to 5 hours with continuous GPS use. 
                       Water-resistant to 50 meters.Syncs with Mac OS X 12.2 and up, iPhone 5S and later, iPad 5 gen. and later, Android 7.0 and later. 
                       Syncing range: Up to 30 feet.International Model - No warranty in the US. In Box: Fitbit Charge 4, Classic wristbands (both small & large), Charging cable.''',"image":"static/fitbit.jpg"},
    
    
    {"id": 6, "name": "Logitech MX Master 3", "price": "$60.00", 
     "description": '''Any-surface tracking - now 8K DPI: Use MX Master 3S cordless computer mouse to work on any surface - even glass - with the upgraded 8000 DPI sensor with customizable sensitivity
                       Introducing quiet clicks: MX Master 3S Bluetooth mouse introduces Quiet Clicks - offering the same satisfying feel but with 90% less click noise
                       Magspeed scrolling: A computer mouse with remarkable speed, precision, and near silence - MagSpeed scrolling is 90% faster, 87% more precise, 
                       and ultra quietErgonomic design: Work comfortably with a precision mouse featuring a silhouette crafted for a more natural wrist posture and optimally placed thumb controls
                       Upgraded customization software: Customize buttons and optimize your workflow with App specific profiles in the improved Logi Option''',"image":"images/logitech.jpg"},
    
    
    {"id": 7, "name": "Sony WH-1000XM4", "price": "$70.00", 
     "description": '''Dual Noise Cancelling for intense musicEXTRA BASS for impressively deep, punchy soundListen all day, charge in minutesEasier, clearer hands-free callingSwitch effortlessly between devices''',"image":"images/sony.jpg"},
    
    
    {"id": 8, "name": "Ring Video Doorbell Pro", "price": "$80.00", 
     "description": '''COMPABILITY- This doorbell transformer is designed for all versions of Ring door bell. 
                       It is compatible with the Ring Video Doorbell, Ring Video Doorbell 2 and Ring Video Doorbell Pro. 
                       A constant power solution and no more interrupted operation well offered for you by this Ring doorbell power adapter.
                       POWER - Power Adapter Input voltage is 120VAC @ 60Hz; Output rating is 18VAC @ 500mA. 
                       Meet Ring products’ official specification.QUALFICATION and DURABILITY - Video Doorbell Power Supply ETL Certificate with high quality construction, the safety product guaranteed for you. 
                       This transformer has passed strict tests to ensure optimal and long term performance for its applications.''',"image":"images/ring.jpg"},
    
    
    {"id": 9, "name": "DJI Mavic Air 2", "price": "$90.00", 
     "description": '''Spacious Storage: Holds 1 drone, 3 batteries, 1 remote controller, 1 battery charger, 1 battery charging hub, power bank adapter,
                       Secure Carrying: Non-slip handle and two action locks keep the case tightly closed using compression force. Suitcase can be padlocked.
                       Portable Size: Dimensions: 35.5 x 30 x 9.5 cm, lightweight at 1.24kg, easy to carry.''',"image":"images/mavic.jpg"},
    
    
    {"id": 10, "name": "Istant Pot Duo 7-in-1", "price": "$100.00", 
     "description": '''VERSATILE INNER COOKING POT: Food-grade stainless-steel cooking pot with a tri-ply bottom offers more even cooking and an anti-spin design that secures the pot for perfect sautéing.
                       COOK FAST OR SLOW: Pressure cook delicious one-pot meals up to 70% faster than traditional cooking methods or slow cook your favorite traditional recipes – just like grandma used to make.
                       QUICK, EASY CLEAN UP: Finger-print resistant, stainless-steel sides and dishwasher-safe lid, inner pot, and accessories.''',"image":"images/pot.jpg"},
    
    
    {"id": 11, "name": "Bose SoundLink Revolve+", "price": "$110.00", 
     "description":'''BOSE SIMPLESYNC TECHNOLOGY: SimpleSync pairs your SoundLink Revolve+ Series II to compatible Bose products for sound that follows you. 
                      BOSE SIMPLESYNC TECHNOLOGY: SimpleSync pairs your SoundLink Revolve+ Series II to compatible Bose products for sound that follows you.
                      BOSE SIMPLESYNC TECHNOLOGY: SimpleSync pairs your SoundLink Revolve+ Series II to compatible Bose products for sound that follows you.''',"image":"images/bose.jpg"},
    
    
    {"id": 12, "name": "Oculus Quest 2", "price": "$120.00", 
     "description": '''T5 Screwdriver, Tweezer, Pry Tool】Our repair kit comes for meta quest 2 controller with a T5 screwdriver, tweezer and pry tool - everything you need for easy and comfortable Meta Quest 2 controller repair. 
                       (Note:Professional installation is highly recommendedComplete Repair Solution】Each replacement kit for quest 2 controller includes all necessary parts and tools to repair your Meta Quest 2 controllers, including 2 x Replacement joystick, 2 x Replacement thumsticks, 4 x Thumb Stick Caps, 1 × Tweezer, 1 × Pry Tool, 1 × Metal Pad Tool, 1 x T5 Screwdriver, 1 x T5 Small Screwdriver''',"image":"images/oculus.jpg"},
    
    
    {"id": 13, "name": "WD 5TB Elements Portable", "price": "$130.00", 
     "description": '''Transfer data at maximum speed with USB 3.0; 
                       USB 2.0 compatiblePlug-and-play ready for Windows PC ''',"image":"images/wd.jpg"},
    
    
    {"id": 14, "name": "GoPro HERO9 Black", "price": "$140.00", 
     "description":'''MORE EVERYTHING. 
                      More power. 
                      More clarity. 
                      More stability. 
                      New Live View Front Display. 
                      30% More Battery Life. Detachable Lens. 
                      Waterproof 33ft.Bundle Includes: 1 x GoPro HERO9 Black with all mfr supplied accessories, 1 x 128GB Micro SDXC Class 10 UHS-1 Memory Card, USB High Speed Card Reader, Water Resistant Case, Selfie Stick, 3-Way Bike Mount, Helmet Front Mount Kit, wrist mount, Mini Suction Cup Mount, Chest Strap, Head Strap, Floating '' Bobber'' ''',"image":"images/gopro.jpg"},
    
    
    {"id": 15, "name": "Philips Hue White and Color Ambiance", "price": "$150.00", 
     "description": '''Music Sync】The Smart LED downlight will change color randomly by reacting to the music rhythm via the microphone built-in your phone. 
                       You can feel the music around you and will have the ultimate real-time immersive audiovisual live experience in a colorful and dynamic.Voice Control】
                       You can easily control the smart ceiling light via voice. Simply use voice commands to turn on or off lights, change light colors, and adjust brightness. 
                       Works with Alexa and Google Assistant for hands-free control.''',"image":"images/phillips.jpg"},
    
    
    {"id": 16, "name": "Anker PowerCore 10000", "price": "$160.00", 
     "description": '''Material:EVA ,Color: Black, 
                       Internal size: 6*3*1inchssFor sale is case only (device and accessories are sold separately)''',"image":"images/anker.jpg"},
    
    
    {"id": 17, "name": "Kindle Paperwhite", "price": "$170.00", 
     "description": '''Anti-slip grip design let you hold your device comfortableMade of durable high quality material''',"image":"images/kindle.jpg"},
    
    
    {"id": 18, "name": "Apple Watch Series 6", "price": "$180.00", 
     "description": '''EASILY CUSTOMIZABLE — With watch bands in a range of styles, materials, and colors and fully customizable watch faces, 
                       You can change your watch to fit your mood or the moment.SWIMPROOF AND STYLISH — 50m water resistance. Three finishes. 
                       And a color-matched back case made with a production process that reduces its carbon emissions.''',"image":"images/apple.jpg"},
    
    
    {"id": 19, "name": "Google Nest Learning Thermostat", "price": "$190.00", 
     "description":'''Home/Away Assist: don't heat or cool an empty home. 
                      Home/Away Assist adjusts the temperature after you leave.
                      Remote control: Control your thermostat from anywhere using the Nest app.''',"image":"images/google.jpg"},
    
    
    {"id": 20, "name": "Razer BlackWidow Elite", "price": "$200.00", 
     "description": '''Ergonomic, Magnetic Wrist Rest: Made of plush leatherette to maximize comfort over extended gaming sessions
                       Durable Construction: Supports up to 80 million clicks with a 2 year manufacturer warranty''',"image":"images/razer.jpg"}
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return render_template('product_detail.html', product=product)
    else:
        return "Product not found", 404

@app.route('/prices')
def prices():
    return render_template('prices.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
