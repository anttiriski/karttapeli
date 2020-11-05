from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://www.jetpunk.com/user-quizzes/33598/maailman-valtioiden-nimet-suomeksi')
driver.set_window_size(1024, 600)
driver.maximize_window()

button = driver.find_element_by_id('start-button')
button.click()

inputField = driver.find_element_by_id('txt-answer-box')

countries = ['Alankomaat', 'Albania', 'Andorra', 'Belgia', 'Bosnia', 'Bulgaria', 'Espanja',
'Irlanti', 'Islanti', 'Italia', 'Itävalta', 'Kosovo', 'Kreikka' 'Kroatia', 'Latvia', 'Liechtenstein',
'Liettua', 'Luxemburg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Norja', 'Makedonia', 'Portugali',
'Puola', 'Ranska', 'Romania', 'Ruotsi', 'Saksa', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia',
'Suomi', 'Sveitsi', 'Tanska', 'Tsekki', 'Ukraina', 'Unkari', 'Valko-Venäjä', 'Vatikaani', 'Venäjä',
'Viro', 'Iso-Britannia', 'Afganistan', 'Armenia', 'Azerbaidzan', 'Bahrain', 'Bangladesh', 'Bhutan',
'Brunei', 'Etelä-Korea', 'Filippiinit', 'Georgia', 'Indonesia', 'Intia', 'Irak', 'Iran', 'Israel',
'Itä-Timor', 'Japani', 'Jemen', 'Jordania', 'Kambodza', 'Kazakstan', 'Kiina', 'Kirgisia', 'Kuwait',
'Kypros', 'Laos', 'Libanon', 'Malediivit', 'Malesia', 'Mongolia', 'Myanmar', 'Nepal', 'Oman', 'Pakistan',
'Pohjois-Korea', 'Qatar', 'Saudi-Arabia', 'Singapore', 'Sri Lanka', 'Syyria', 'Tadzikistan', 'Taiwan', 
'Thaimaa', 'Turkki', 'Turkmenistan', 'Uzbekistan', 'Vietnam', 'Yhdistyneet arabiemiirikunnat', 'Algeria',
'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Djibouti', 'Egypti', 'Eritrea', 'Etelä-Afrikka', 
'Etelä-Sudan', 'Etiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Kamerun', 'Kap Verde', 'Kenia',
'Keski-Afrikka', 'Komorit', 'Kongo', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Marokko',
'Mauritania', 'Mauritius', 'Mosambik', 'Namibia', 'Niger', 'Nigeria', 'Norsunluurannikko', 'Päiväntasaajan Guinea',
'Ruanda', 'Sambia', 'Sao Tome', 'Senegal', 'Seychellit', 'Sierra Leone', 'Somalia', 'Sudan', 'Swazimaa', 'Tansania',
'Togo', 'Tsad', 'Tunisia', 'Uganda', 'Zimbabwe', 'Antigua', 'Bahama', 'Barbados', 'Belize', 'Costa Rica', 'Dominica',
'Dominikaaninen tasavalta', 'El Salvador', 'Grenada', 'Guatemala', 'Haiti', 'Honduras', 'Jamaika', 'Kanada', 'Kuuba', 
'Meksiko', 'Nicaragua', 'Panama', 'Saint Kitts', 'Saint Lucia', 'Saint Vincent', 'Trinidad', 'USA', 'Argentiina', 'Bolivia',
'Brasilia', 'Chile', 'Ecuador', 'Guyana', 'Kolumbia', 'Paraguay', 'Uruguay', 'Peru', 'Surinam', 'Venezuela', 'Australia',
'Fidzi', 'Kiribati', 'Marshallinsaaret', 'Mikronesia', 'Nauru', 'Palau', 'Papua', 'Salomonsaaret', 'Samoa', 'Tonga',
'Tuvalu', 'Uusi-Seelanti', 'Vanuatu'
]

for country in countries:
    inputField.send_keys(country)
