# MessageSys Django-projekt

## Indstillinger (settings.py)

### Generelle indstillinger

- **Base Directory**: Alle stier i projektet er bygget oven på denne base.
- **Locale Paths**: Benyttes til internationalisering og lokalisering.
- **Secret Key**: Udsættes ikke, da den trækkes fra en miljøvariabel.
- **Debug Mode**: Aktiveret (`True`), bør ikke bruges i produktion.
- **Login URL**: "login" er URL'en, der håndterer login.

### Tilladte Værter

- `sendsms.unord.dk`

### Sikkerhedsindstillinger

- **CSRF Trusted Origins**: `https://sendsms.unord.dk`
  
### Installerede Apps

- Standard Django-apps som `admin`, `auth`, osv.
- `rest_framework` til REST API.
- Tredjeparts-apps:
  - `bootstrap_datepicker_plus` til datovælger.
- Egne apps:
  - `sms_app`, `pages_app`, `authenticate_app`.

### Middleware

- Standard Django-middleware til sikkerhed, sessionhåndtering, osv.

### Database

- PostgreSQL er databasemotoren.
- Konfiguration udsættes ikke, da den trækkes fra miljøvariabler.

### Tidszone og Sprog

- Sprogkode: `da`
- Tidszone: `Europe/Copenhagen`

---

## Autentificering App (authenticate_app)

### Views (views.py)

1. **SignIn View**: Benytter `SignUpForm` til at håndtere brugeroprettelse.
2. **EditProfile View**: Benytter `EditProfileForm` til at håndtere profilredigering.
3. **ChangePassword View**: Benytter `ChangePasswordForm` til at håndtere ændring af adgangskode.

---

## Afhængigheder (requirements.txt)

Projektet anvender følgende Python-biblioteker, som er angivet i `requirements.txt`:

- **Django==4.1.5**: Hovedrammeverket for webapplikationen.
- **django-extensions==3.2.1**: Udvidelser til Django for at forbedre udviklingsprocessen.
- **djangorestframework==3.14.0**: Bruges til at oprette RESTful API'er med Django.
- **django-bootstrap-datepicker-plus==5.0.3**: Implementerer en datovælger komponent med Bootstrap.
- **numpy==1.24.1**: Matematikbibliotek, anvendt for numeriske operationer.
- **openpyxl==3.0.10**: Bruges til at læse fra og skrive til Excel-filer.
- **python-decouple==3.7**: Håndterer miljøvariabler og konfiguration separat fra koden.
- **psycopg2-binary==2.9.5**: PostgreSQL database adapter for Python.
- **pandas==1.5.2**: Dataanalysebibliotek, ofte brugt for data manipulation.
- **requests==2.28.2**: Bruges til at sende HTTP-anmodninger.
- **xlrd==2.0.1**: Bruges til at læse data fra ældre Excel-filer.

### Installation

For at installere alle de nødvendige pakker, kør følgende kommando i din terminal:

```
pip install -r requirements.txt
```

Dette vil installere alle de nødvendige afhængigheder og gøre det lettere for andre udviklere at forstå, hvad hver pakke gør i dit projekt.

---

## `sms_app`

### Introduktion

Dette Django-projekt kaldet `sms_app` bruges til at sende, modtage og administrere SMS-beskeder. Det gør brug af Django's indbyggede generic views og har også brugeradgangskontrol via `login_required` dekoratører.

### Filstruktur

- `models.py`: Indeholder Django modeller som `Message` og `Recipient`.
- `views.py`: Indeholder logik til at håndtere HTTP-anmodninger.
- `forms.py`: Definerer Django formularer til brugerinput.
- `unord_mail.py` og `unord_sms.py`: Håndterer henholdsvis mail og SMS-funktionaliteter.

### Sådan fungerer det

#### Generelle Klasser

1. **MessageListView**: Viser en liste over meddelelser.
2. **MessageCreateView**: Opretter en ny meddelelse.
3. **MessageDetailView**: Viser detaljer om en enkelt meddelelse, herunder modtagere.
4. **MessageUpdateView**: Tillader redigering af en eksisterende meddelelse.
5. **MessageDeleteView**: Sletter en meddelelse.

#### Funktioner

1. **approve_sms**: Godkender en meddelelse til afsendelse.
2. **reject_sms**: Afviser og sletter en meddelelse.
3. **import_data**: Importerer modtagerdata fra en Excel-fil.

### Ekstra Information

- **Django Views**: Vi bruger `@method_decorator(login_required, name='dispatch')` for at sikre, at kun logget ind brugere kan få adgang til visse views.
  
- **Pandas**: Bruges til at behandle Excel-filer.

- **Email & SMS Integration**: `unord_mail` og `unord_sms` filerne indeholder logik for afsendelse af e-mails og SMS'er.

- **Model Fields**: `Message` model inkluderer et `user` felt, der er en CharField. Det er tilknyttet brugeren, der opretter meddelelsen.

### Databasestruktur

#### `Message` Model

- `id`: Primærnøgle, autogenereret
- `email`: E-mailadresse, `CharField`
- `message`: Beskeden der skal sendes, `CharField`
- `link_code`: En tilfældig genereret kode til at godkende beskeden, `CharField`
- `time_to_send`: Tidspunktet, hvor beskeden skal sendes, `DateTimeField`
- `user`: Bruger, der oprettede beskeden, `ForeignKey til User model`
  
Relation: One-to-Many til `Recipient` via `message_id`

#### `Recipient` Model

- `id`: Primærnøgle, autogenereret
- `message`: Foreign key til `Message` model, `ForeignKey`
- `mobile_number`: Mobilnummer for modtager, `CharField`
- `first_name`: Fornavn på modtager, `CharField`
- `last_name`: Efternavn på modtager, `CharField`

### Installation og Kørsel

1. Clone repositoriet.
2. Installer afhængigheder med `pip install -r requirements.txt`.
3. Kør `python manage.py migrate` for at initialisere databasen.
4. Kør `python manage.py runserver` for at starte udviklingsserveren.

### FAQ

- **Hvorfor ser jeg en "Fil fejl" i `import_data` metoden?**

  - Dette kan ske, hvis Excel-filen har tomme rækker eller kolonner.

- **Hvad gør `letters_to_numbers` funktionen?**

  - Den konverterer en bogstavkolonnebetegnelse til et kolonnenummer (f.eks., "A" bliver til 1, "Z" til 26). Det bruges så pandas nemer kan finde den rette celle. 

