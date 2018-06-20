# Getting started

Ytel API version 3

## How to Build


You must have Python ```2 >=2.7.9``` or Python ```3 >=3.4``` installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. 
These dependencies are defined in the ```requirements.txt``` file that comes with the SDK.
To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type ```pip --version```.
This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including ```requirements.txt```) for the SDK.
* Run the command ```pip install -r requirements.txt```. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?step=installDependencies&workspaceFolder=Ytel%20API-Python)


## How to Use

The following section explains how to use the Ytelapi SDK package in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=pyCharm)

Click on ```Open``` in PyCharm to browse to your generated SDK directory and then click ```OK```.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=openProject0&workspaceFolder=Ytel%20API-Python)     

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=openProject1&workspaceFolder=Ytel%20API-Python&projectName=ytelapi)     

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=createDirectory&workspaceFolder=Ytel%20API-Python&projectName=ytelapi)

Name the directory as "test"

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=nameDirectory)
   
Add a python file to this project with the name "testsdk"

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=createFile&workspaceFolder=Ytel%20API-Python&projectName=ytelapi)

Name it "testsdk"

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```Python
from ytelapi.ytelapi_client import YtelapiClient
```

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=Ytel%20API-Python&libraryName=ytelapi.ytelapi_client&projectName=ytelapi&className=YtelapiClient)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on ```Run```

![Run Test Project - Step 1](https://apidocs.io/illustration/python?step=runProject&workspaceFolder=Ytel%20API-Python&libraryName=ytelapi.ytelapi_client&projectName=ytelapi&className=YtelapiClient)


## How to Test

You can test the generated SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke ```pip install -r test-requirements.txt```
  3. Invoke ```nosetests```

## Initialization

### Authentication
In order to setup authentication and initialization of the API client, you need the following information.

| Parameter | Description |
|-----------|-------------|
| basic_auth_user_name | The username to use with basic authentication |
| basic_auth_password | The password to use with basic authentication |



API client can be initialized as following.

```python
# Configuration parameters and credentials
basic_auth_user_name = 'basic_auth_user_name' # The username to use with basic authentication
basic_auth_password = 'basic_auth_password' # The password to use with basic authentication

client = YtelapiClient(basic_auth_user_name, basic_auth_password)
```



# Class Reference

## <a name="list_of_controllers"></a>List of Controllers

* [ShortCodeController](#short_code_controller)
* [AreaMailController](#area_mail_controller)
* [PostCardController](#post_card_controller)
* [LetterController](#letter_controller)
* [CallController](#call_controller)
* [PhoneNumberController](#phone_number_controller)
* [SMSController](#sms_controller)
* [SharedShortCodeController](#shared_short_code_controller)
* [ConferenceController](#conference_controller)
* [CarrierController](#carrier_controller)
* [EmailController](#email_controller)
* [AccountController](#account_controller)
* [SubAccountController](#sub_account_controller)
* [AddressController](#address_controller)
* [RecordingController](#recording_controller)
* [TranscriptionController](#transcription_controller)
* [UsageController](#usage_controller)

## <a name="short_code_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ShortCodeController") ShortCodeController

### Get controller instance

An instance of the ``` ShortCodeController ``` class can be accessed from the API Client.

```python
 short_code_controller = client.short_code
```

### <a name="create_dedicatedshortcode_listshortcode"></a>![Method: ](https://apidocs.io/img/method.png ".ShortCodeController.create_dedicatedshortcode_listshortcode") create_dedicatedshortcode_listshortcode

> Retrieve a list of Short Code assignment associated with your Ytel account.

```python
def create_dedicatedshortcode_listshortcode(self,
                                                options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| shortcode |  ``` Optional ```  | Only list Short Code Assignment sent from this Short Code |
| page |  ``` Optional ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pagesize |  ``` Optional ```  | The count of objects to return per page. |



#### Example Usage

```python
collect = {}

shortcode = 'Shortcode'
collect['shortcode'] = shortcode

page = 'page'
collect['page'] = page

pagesize = 'pagesize'
collect['pagesize'] = pagesize


result = short_code_controller.create_dedicatedshortcode_listshortcode(collect)

```


### <a name="create_dedicatedshortcode_updateshortcode"></a>![Method: ](https://apidocs.io/img/method.png ".ShortCodeController.create_dedicatedshortcode_updateshortcode") create_dedicatedshortcode_updateshortcode

> Update a dedicated shortcode.

```python
def create_dedicatedshortcode_updateshortcode(self,
                                                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| shortcode |  ``` Required ```  | List of valid dedicated shortcode to your Ytel account. |
| friendlyName |  ``` Optional ```  | User generated name of the dedicated shortcode. |
| callbackMethod |  ``` Optional ```  | Specifies the HTTP method used to request the required StatusCallBackUrl once call connects. |
| callbackUrl |  ``` Optional ```  | URL that can be requested to receive notification when call has ended. A set of default parameters will be sent here once the call is finished. |
| fallbackMethod |  ``` Optional ```  | Specifies the HTTP method used to request the required FallbackUrl once call connects. |
| fallbackUrl |  ``` Optional ```  | URL used if any errors occur during execution of InboundXML or at initial request of the required Url provided with the POST. |



#### Example Usage

```python
collect = {}

shortcode = 'Shortcode'
collect['shortcode'] = shortcode

friendly_name = 'FriendlyName'
collect['friendly_name'] = friendly_name

callback_method = 'CallbackMethod'
collect['callback_method'] = callback_method

callback_url = 'CallbackUrl'
collect['callback_url'] = callback_url

fallback_method = 'FallbackMethod'
collect['fallback_method'] = fallback_method

fallback_url = 'FallbackUrl'
collect['fallback_url'] = fallback_url


result = short_code_controller.create_dedicatedshortcode_updateshortcode(collect)

```


### <a name="create_dedicatedshortcode_viewshortcode"></a>![Method: ](https://apidocs.io/img/method.png ".ShortCodeController.create_dedicatedshortcode_viewshortcode") create_dedicatedshortcode_viewshortcode

> Retrieve a single Short Code object by its shortcode assignment.

```python
def create_dedicatedshortcode_viewshortcode(self,
                                                shortcode)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| shortcode |  ``` Required ```  | List of valid Dedicated Short Code to your Ytel account |



#### Example Usage

```python
shortcode = 'Shortcode'

result = short_code_controller.create_dedicatedshortcode_viewshortcode(shortcode)

```


### <a name="create_shortcode_viewsms"></a>![Method: ](https://apidocs.io/img/method.png ".ShortCodeController.create_shortcode_viewsms") create_shortcode_viewsms

> View a single Sms Short Code message.

```python
def create_shortcode_viewsms(self,
                                 message_sid)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| messageSid |  ``` Required ```  | The unique identifier for the sms resource |



#### Example Usage

```python
message_sid = 'MessageSid'

result = short_code_controller.create_shortcode_viewsms(message_sid)

```


### <a name="create_dedicatedshortcode_getinboundsms"></a>![Method: ](https://apidocs.io/img/method.png ".ShortCodeController.create_dedicatedshortcode_getinboundsms") create_dedicatedshortcode_getinboundsms

> Retrive a list of inbound Sms Short Code messages associated with your Ytel account.

```python
def create_dedicatedshortcode_getinboundsms(self,
                                                options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | Number of individual resources listed in the response per page |
| mfrom |  ``` Optional ```  | Only list SMS messages sent from this number |
| shortcode |  ``` Optional ```  | Only list SMS messages sent to Shortcode |
| datecreated |  ``` Optional ```  | Only list SMS messages sent in the specified date MAKE REQUEST |



#### Example Usage

```python
collect = {}

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize

mfrom = 'From'
collect['mfrom'] = mfrom

shortcode = 'Shortcode'
collect['shortcode'] = shortcode

datecreated = 'Datecreated'
collect['datecreated'] = datecreated


result = short_code_controller.create_dedicatedshortcode_getinboundsms(collect)

```


### <a name="create_dedicatedshortcode_sendsms"></a>![Method: ](https://apidocs.io/img/method.png ".ShortCodeController.create_dedicatedshortcode_sendsms") create_dedicatedshortcode_sendsms

> Send Dedicated Shortcode

```python
def create_dedicatedshortcode_sendsms(self,
                                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| shortcode |  ``` Required ```  | Your dedicated shortcode |
| to |  ``` Required ```  | The number to send your SMS to |
| body |  ``` Required ```  | The body of your message |
| method |  ``` Optional ```  | Specifies the HTTP method used to request the required URL once the Short Code message is sent.GET or POST |
| messagestatuscallback |  ``` Optional ```  | URL that can be requested to receive notification when Short Code message was sent. |



#### Example Usage

```python
collect = {}

shortcode = 209
collect['shortcode'] = shortcode

to = 209.709060110482
collect['to'] = to

body = 'body'
collect['body'] = body

method = 'method'
collect['method'] = method

messagestatuscallback = 'messagestatuscallback'
collect['messagestatuscallback'] = messagestatuscallback


result = short_code_controller.create_dedicatedshortcode_sendsms(collect)

```


### <a name="create_shortcode_listsms"></a>![Method: ](https://apidocs.io/img/method.png ".ShortCodeController.create_shortcode_listsms") create_shortcode_listsms

> Retrieve a list of Short Code messages.

```python
def create_shortcode_listsms(self,
                                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| shortcode |  ``` Optional ```  | Only list messages sent from this Short Code |
| to |  ``` Optional ```  | Only list messages sent to this number |
| dateSent |  ``` Optional ```  | Only list messages sent with the specified date |
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pageSize |  ``` Optional ```  ``` DefaultValue ```  | The count of objects to return per page. |



#### Example Usage

```python
collect = {}

shortcode = 'Shortcode'
collect['shortcode'] = shortcode

to = 'To'
collect['to'] = to

date_sent = 'DateSent'
collect['date_sent'] = date_sent

page = 1
collect['page'] = page

page_size = 10
collect['page_size'] = page_size


result = short_code_controller.create_shortcode_listsms(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="area_mail_controller"></a>![Class: ](https://apidocs.io/img/class.png ".AreaMailController") AreaMailController

### Get controller instance

An instance of the ``` AreaMailController ``` class can be accessed from the API Client.

```python
 area_mail_controller = client.area_mail
```

### <a name="create_areamail_delete"></a>![Method: ](https://apidocs.io/img/method.png ".AreaMailController.create_areamail_delete") create_areamail_delete

> Remove an AreaMail object by its AreaMailId.

```python
def create_areamail_delete(self,
                               areamailid)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| areamailid |  ``` Required ```  | The unique identifier for an AreaMail object. |



#### Example Usage

```python
areamailid = 'areamailid'

result = area_mail_controller.create_areamail_delete(areamailid)

```


### <a name="create_areamail_create"></a>![Method: ](https://apidocs.io/img/method.png ".AreaMailController.create_areamail_create") create_areamail_create

> Create a new AreaMail object.

```python
def create_areamail_create(self,
                               options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| routes |  ``` Required ```  | List of routes that AreaMail should be delivered to.  A single route can be either a zipcode or a carrier route.List of routes that AreaMail should be delivered to.  A single route can be either a zipcode or a carrier route. A carrier route is in the form of 92610-C043 where the carrier route is composed of 5 numbers for zipcode, 1 letter for carrier route type, and 3 numbers for carrier route code. Delivery can be sent to mutliple routes by separating them with a commas. Valid Values: 92656, 92610-C043 |
| attachbyid |  ``` Required ```  | Set an existing areamail by attaching its AreamailId. |
| front |  ``` Required ```  | The front of the AreaMail item to be created. This can be a URL, local file, or an HTML string. Supported file types are PDF, PNG, and JPEG. Back required |
| back |  ``` Required ```  | The back of the AreaMail item to be created. This can be a URL, local file, or an HTML string. Supported file types are PDF, PNG, and JPEG. |
| description |  ``` Optional ```  | A string value to use as a description for this AreaMail item. |
| targettype |  ``` Optional ```  | The delivery location type. |
| htmldata |  ``` Optional ```  | A string value that contains HTML markup. |



#### Example Usage

```python
collect = {}

routes = 'routes'
collect['routes'] = routes

attachbyid = 'attachbyid'
collect['attachbyid'] = attachbyid

front = 'front'
collect['front'] = front

back = 'back'
collect['back'] = back

description = 'description'
collect['description'] = description

targettype = 'targettype'
collect['targettype'] = targettype

htmldata = 'htmldata'
collect['htmldata'] = htmldata


result = area_mail_controller.create_areamail_create(collect)

```


### <a name="create_areamail_view"></a>![Method: ](https://apidocs.io/img/method.png ".AreaMailController.create_areamail_view") create_areamail_view

> Retrieve an AreaMail object by its AreaMailId.

```python
def create_areamail_view(self,
                             areamailid)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| areamailid |  ``` Required ```  | The unique identifier for an AreaMail object. |



#### Example Usage

```python
areamailid = 'areamailid'

result = area_mail_controller.create_areamail_view(areamailid)

```


### <a name="create_areamail_lists"></a>![Method: ](https://apidocs.io/img/method.png ".AreaMailController.create_areamail_lists") create_areamail_lists

> Retrieve a list of AreaMail objects.

```python
def create_areamail_lists(self,
                              options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | The count of objects to return per page. |
| areamailsid |  ``` Optional ```  | The unique identifier for an AreaMail object. |
| dateCreated |  ``` Optional ```  | The date the AreaMail was created. |



#### Example Usage

```python
collect = {}

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize

areamailsid = 'areamailsid'
collect['areamailsid'] = areamailsid

date_created = 'dateCreated'
collect['date_created'] = date_created


result = area_mail_controller.create_areamail_lists(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="post_card_controller"></a>![Class: ](https://apidocs.io/img/class.png ".PostCardController") PostCardController

### Get controller instance

An instance of the ``` PostCardController ``` class can be accessed from the API Client.

```python
 post_card_controller = client.post_card
```

### <a name="postcard_deletepostcard"></a>![Method: ](https://apidocs.io/img/method.png ".PostCardController.postcard_deletepostcard") postcard_deletepostcard

> Remove a postcard object.

```python
def postcard_deletepostcard(self,
                                postcardid)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| postcardid |  ``` Required ```  | The unique identifier of a postcard object. |



#### Example Usage

```python
postcardid = 'postcardid'

result = post_card_controller.postcard_deletepostcard(postcardid)

```


### <a name="postcard_viewpostcard"></a>![Method: ](https://apidocs.io/img/method.png ".PostCardController.postcard_viewpostcard") postcard_viewpostcard

> Retrieve a postcard object by its PostcardId.

```python
def postcard_viewpostcard(self,
                              postcardid)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| postcardid |  ``` Required ```  | The unique identifier for a postcard object. |



#### Example Usage

```python
postcardid = 'postcardid'

result = post_card_controller.postcard_viewpostcard(postcardid)

```


### <a name="postcard_listpostcard"></a>![Method: ](https://apidocs.io/img/method.png ".PostCardController.postcard_listpostcard") postcard_listpostcard

> Retrieve a list of postcard objects. The postcards objects are sorted by creation date, with the most recently created postcards appearing first.

```python
def postcard_listpostcard(self,
                              options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | The count of objects to return per page. |
| postcardid |  ``` Optional ```  | The unique identifier for a postcard object. |
| dateCreated |  ``` Optional ```  | The date the postcard was created. |



#### Example Usage

```python
collect = {}

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize

postcardid = 'postcardid'
collect['postcardid'] = postcardid

date_created = 'dateCreated'
collect['date_created'] = date_created


result = post_card_controller.postcard_listpostcard(collect)

```


### <a name="postcard_createpostcard"></a>![Method: ](https://apidocs.io/img/method.png ".PostCardController.postcard_createpostcard") postcard_createpostcard

> Create, print, and mail a postcard to an address. The postcard front must be supplied as a PDF, image, or an HTML string. The back can be a PDF, image, HTML string, or it can be automatically generated by supplying a custom message.

```python
def postcard_createpostcard(self,
                                options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| to |  ``` Required ```  | The AddressId or an object structured when creating an address by addresses/Create. |
| mfrom |  ``` Required ```  | The AddressId or an object structured when creating an address by addresses/Create. |
| attachbyid |  ``` Required ```  | Set an existing postcard by attaching its PostcardId. |
| front |  ``` Required ```  | A 4.25"x6.25" or 6.25"x11.25" image to use as the front of the postcard.  This can be a URL, local file, or an HTML string. Supported file types are PDF, PNG, and JPEG. |
| back |  ``` Required ```  | A 4.25"x6.25" or 6.25"x11.25" image to use as the back of the postcard, supplied as a URL, local file, or HTML string.  This allows you to customize your back design, but we will still insert the recipient address for you. |
| message |  ``` Required ```  | The message for the back of the postcard with a maximum of 350 characters. |
| setting |  ``` Required ```  | Code for the dimensions of the media to be printed. |
| description |  ``` Optional ```  | A description for the postcard. |
| htmldata |  ``` Optional ```  | A string value that contains HTML markup. |



#### Example Usage

```python
collect = {}

to = 'to'
collect['to'] = to

mfrom = 'from'
collect['mfrom'] = mfrom

attachbyid = 'attachbyid'
collect['attachbyid'] = attachbyid

front = 'front'
collect['front'] = front

back = 'back'
collect['back'] = back

message = 'message'
collect['message'] = message

setting = 'setting'
collect['setting'] = setting

description = 'description'
collect['description'] = description

htmldata = 'htmldata'
collect['htmldata'] = htmldata


result = post_card_controller.postcard_createpostcard(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="letter_controller"></a>![Class: ](https://apidocs.io/img/class.png ".LetterController") LetterController

### Get controller instance

An instance of the ``` LetterController ``` class can be accessed from the API Client.

```python
 letter_controller = client.letter
```

### <a name="create_letter_delete"></a>![Method: ](https://apidocs.io/img/method.png ".LetterController.create_letter_delete") create_letter_delete

> Remove a letter object by its LetterId.

```python
def create_letter_delete(self,
                             lettersid)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| lettersid |  ``` Required ```  | The unique identifier for a letter object. |



#### Example Usage

```python
lettersid = 'lettersid'

result = letter_controller.create_letter_delete(lettersid)

```


### <a name="create_letter_viewletter"></a>![Method: ](https://apidocs.io/img/method.png ".LetterController.create_letter_viewletter") create_letter_viewletter

> Retrieve a letter object by its LetterSid.

```python
def create_letter_viewletter(self,
                                 lettersid)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| lettersid |  ``` Required ```  | The unique identifier for a letter object. |



#### Example Usage

```python
lettersid = 'lettersid'

result = letter_controller.create_letter_viewletter(lettersid)

```


### <a name="create_letter_listsletter"></a>![Method: ](https://apidocs.io/img/method.png ".LetterController.create_letter_listsletter") create_letter_listsletter

> Retrieve a list of letter objects. The letter objects are sorted by creation date, with the most recently created letters appearing first.

```python
def create_letter_listsletter(self,
                                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | The count of objects to return per page. |
| lettersid |  ``` Optional ```  | The unique identifier for a letter object. |
| dateCreated |  ``` Optional ```  | The date the letter was created. |



#### Example Usage

```python
collect = {}

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize

lettersid = 'lettersid'
collect['lettersid'] = lettersid

date_created = 'dateCreated'
collect['date_created'] = date_created


result = letter_controller.create_letter_listsletter(collect)

```


### <a name="create_letter_create"></a>![Method: ](https://apidocs.io/img/method.png ".LetterController.create_letter_create") create_letter_create

> Create, print, and mail a letter to an address. The letter file must be supplied as a PDF or an HTML string.

```python
def create_letter_create(self,
                             options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| to |  ``` Required ```  | The AddressId or an object structured when creating an address by addresses/Create. |
| mfrom |  ``` Required ```  | The AddressId or an object structured when creating an address by addresses/Create. |
| attachbyid |  ``` Required ```  | Set an existing letter by attaching its LetterId. |
| file |  ``` Required ```  | File can be a 8.5"x11" PDF uploaded file or URL that links to a file. |
| color |  ``` Required ```  | Specify if letter should be printed in color. |
| description |  ``` Optional ```  | A description for the letter. |
| extraservice |  ``` Optional ```  | Add an extra service to your letter. Options are "certified" or "registered". Certified provides tracking and delivery confirmation for domestic destinations and is an additional $5.00. Registered provides tracking and confirmation for international addresses and is an additional $16.50. |
| doublesided |  ``` Optional ```  | Specify if letter should be printed on both sides. |
| template |  ``` Optional ```  | Boolean that defaults to true. When set to false, this specifies that your letter does not follow the m360 address template. In this case, a blank address page will be inserted at the beginning of your file and you will be charged for the extra page. |
| htmldata |  ``` Optional ```  | A string value that contains HTML markup. |



#### Example Usage

```python
collect = {}

to = 'to'
collect['to'] = to

mfrom = 'from'
collect['mfrom'] = mfrom

attachbyid = 'attachbyid'
collect['attachbyid'] = attachbyid

file = 'file'
collect['file'] = file

color = 'color'
collect['color'] = color

description = 'description'
collect['description'] = description

extraservice = 'extraservice'
collect['extraservice'] = extraservice

doublesided = 'doublesided'
collect['doublesided'] = doublesided

template = 'template'
collect['template'] = template

htmldata = 'htmldata'
collect['htmldata'] = htmldata


result = letter_controller.create_letter_create(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="call_controller"></a>![Class: ](https://apidocs.io/img/class.png ".CallController") CallController

### Get controller instance

An instance of the ``` CallController ``` class can be accessed from the API Client.

```python
 call_controller = client.call
```

### <a name="create_calls_viewcalldetail"></a>![Method: ](https://apidocs.io/img/method.png ".CallController.create_calls_viewcalldetail") create_calls_viewcalldetail

> Retrieve a single voice call’s information by its CallSid.

```python
def create_calls_viewcalldetail(self,
                                    call_sid)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| callSid |  ``` Required ```  | The unique identifier for the voice call. |



#### Example Usage

```python
call_sid = 'callSid'

result = call_controller.create_calls_viewcalldetail(call_sid)

```


### <a name="create_calls_viewcalls"></a>![Method: ](https://apidocs.io/img/method.png ".CallController.create_calls_viewcalls") create_calls_viewcalls

> Retrieve a single voice call’s information by its CallSid.

```python
def create_calls_viewcalls(self,
                               callsid)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| callsid |  ``` Required ```  | The unique identifier for the voice call. |



#### Example Usage

```python
callsid = 'callsid'

result = call_controller.create_calls_viewcalls(callsid)

```


### <a name="create_calls_senddigits"></a>![Method: ](https://apidocs.io/img/method.png ".CallController.create_calls_senddigits") create_calls_senddigits

> Play Dtmf and send the Digit

```python
def create_calls_senddigits(self,
                                options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| callSid |  ``` Required ```  | The unique identifier of each call resource |
| playDtmf |  ``` Required ```  | DTMF digits to play to the call. 0-9, #, *, W, or w |
| playDtmfDirection |  ``` Optional ```  | The leg of the call DTMF digits should be sent to |



#### Example Usage

```python
collect = {}

call_sid = 'CallSid'
collect['call_sid'] = call_sid

play_dtmf = 'PlayDtmf'
collect['play_dtmf'] = play_dtmf

play_dtmf_direction = PlayDtmfDirectionEnum.IN
collect['play_dtmf_direction'] = play_dtmf_direction


result = call_controller.create_calls_senddigits(collect)

```


### <a name="create_calls_makervm"></a>![Method: ](https://apidocs.io/img/method.png ".CallController.create_calls_makervm") create_calls_makervm

> Initiate an outbound Ringless Voicemail through Ytel.

```python
def create_calls_makervm(self,
                             options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| mfrom |  ``` Required ```  | A valid Ytel Voice enabled number (E.164 format) that will be initiating the phone call. |
| rVMCallerId |  ``` Required ```  | A required secondary Caller ID for RVM to work. |
| to |  ``` Required ```  | A valid number (E.164 format) that will receive the phone call. |
| voiceMailURL |  ``` Required ```  | The URL requested once the RVM connects. A set of default parameters will be sent here. |
| method |  ``` Optional ```  ``` DefaultValue ```  | Specifies the HTTP method used to request the required URL once call connects. |
| statusCallBackUrl |  ``` Optional ```  | URL that can be requested to receive notification when call has ended. A set of default parameters will be sent here once the call is finished. |
| statsCallBackMethod |  ``` Optional ```  | Specifies the HTTP method used to request the required StatusCallBackUrl once call connects. |



#### Example Usage

```python
collect = {}

mfrom = 'From'
collect['mfrom'] = mfrom

rvm_caller_id = 'RVMCallerId'
collect['rvm_caller_id'] = rvm_caller_id

to = 'To'
collect['to'] = to

voice_mail_url = 'VoiceMailURL'
collect['voice_mail_url'] = voice_mail_url

method = 'GET'
collect['method'] = method

status_call_back_url = 'StatusCallBackUrl'
collect['status_call_back_url'] = status_call_back_url

stats_call_back_method = 'StatsCallBackMethod'
collect['stats_call_back_method'] = stats_call_back_method


result = call_controller.create_calls_makervm(collect)

```


### <a name="create_calls_listcalls"></a>![Method: ](https://apidocs.io/img/method.png ".CallController.create_calls_listcalls") create_calls_listcalls

> A list of calls associated with your Ytel account

```python
def create_calls_listcalls(self,
                               options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pageSize |  ``` Optional ```  ``` DefaultValue ```  | Number of individual resources listed in the response per page |
| to |  ``` Optional ```  | Filter calls that were sent to this 10-digit number (E.164 format). |
| mfrom |  ``` Optional ```  | Filter calls that were sent from this 10-digit number (E.164 format). |
| dateCreated |  ``` Optional ```  | Return calls that are from a specified date. |



#### Example Usage

```python
collect = {}

page = 1
collect['page'] = page

page_size = 10
collect['page_size'] = page_size

to = 'To'
collect['to'] = to

mfrom = 'From'
collect['mfrom'] = mfrom

date_created = 'DateCreated'
collect['date_created'] = date_created


result = call_controller.create_calls_listcalls(collect)

```


### <a name="create_calls_interruptcalls"></a>![Method: ](https://apidocs.io/img/method.png ".CallController.create_calls_interruptcalls") create_calls_interruptcalls

> Interrupt the Call by Call Sid

```python
def create_calls_interruptcalls(self,
                                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| callSid |  ``` Required ```  | The unique identifier for voice call that is in progress. |
| url |  ``` Optional ```  | URL the in-progress call will be redirected to |
| method |  ``` Optional ```  | The method used to request the above Url parameter |
| status |  ``` Optional ```  | Status to set the in-progress call to |



#### Example Usage

```python
collect = {}

call_sid = 'CallSid'
collect['call_sid'] = call_sid

url = 'Url'
collect['url'] = url

method = 'Method'
collect['method'] = method

status = Status24Enum.CANCELED
collect['status'] = status


result = call_controller.create_calls_interruptcalls(collect)

```


### <a name="create_calls_recordcalls"></a>![Method: ](https://apidocs.io/img/method.png ".CallController.create_calls_recordcalls") create_calls_recordcalls

> Start or stop recording of an in-progress voice call.

```python
def create_calls_recordcalls(self,
                                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| callSid |  ``` Required ```  | The unique identifier of each call resource |
| record |  ``` Required ```  | Set true to initiate recording or false to terminate recording |
| direction |  ``` Optional ```  | The leg of the call to record |
| timeLimit |  ``` Optional ```  | Time in seconds the recording duration should not exceed |
| callBackUrl |  ``` Optional ```  | URL consulted after the recording completes |
| fileformat |  ``` Optional ```  | Format of the recording file. Can be .mp3 or .wav |



#### Example Usage

```python
collect = {}

call_sid = 'CallSid'
collect['call_sid'] = call_sid

record = False
collect['record'] = record

direction = DirectionEnum.IN
collect['direction'] = direction

time_limit = 46
collect['time_limit'] = time_limit

call_back_url = 'CallBackUrl'
collect['call_back_url'] = call_back_url

fileformat = FileformatEnum.MP3
collect['fileformat'] = fileformat


result = call_controller.create_calls_recordcalls(collect)

```


### <a name="create_calls_playaudios"></a>![Method: ](https://apidocs.io/img/method.png ".CallController.create_calls_playaudios") create_calls_playaudios

> Play Audio from a url

```python
def create_calls_playaudios(self,
                                options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| callSid |  ``` Required ```  | The unique identifier of each call resource |
| audioUrl |  ``` Required ```  | URL to sound that should be played. You also can add more than one audio file using semicolons e.g. http://example.com/audio1.mp3;http://example.com/audio2.wav |
| sayText |  ``` Required ```  | Valid alphanumeric string that should be played to the In-progress call. |
| length |  ``` Optional ```  | Time limit in seconds for audio play back |
| direction |  ``` Optional ```  | The leg of the call audio will be played to |
| mix |  ``` Optional ```  | If false, all other audio will be muted |



#### Example Usage

```python
collect = {}

call_sid = 'CallSid'
collect['call_sid'] = call_sid

audio_url = 'AudioUrl'
collect['audio_url'] = audio_url

say_text = 'SayText'
collect['say_text'] = say_text

length = 46
collect['length'] = length

direction = DirectionEnum.IN
collect['direction'] = direction

mix = False
collect['mix'] = mix


result = call_controller.create_calls_playaudios(collect)

```


### <a name="create_calls_voiceeffect"></a>![Method: ](https://apidocs.io/img/method.png ".CallController.create_calls_voiceeffect") create_calls_voiceeffect

> Add audio voice effects to the an in-progress voice call.

```python
def create_calls_voiceeffect(self,
                                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| callSid |  ``` Required ```  | The unique identifier for the in-progress voice call. |
| audioDirection |  ``` Optional ```  | The direction the audio effect should be placed on. If IN, the effects will occur on the incoming audio stream. If OUT, the effects will occur on the outgoing audio stream. |
| pitchSemiTones |  ``` Optional ```  | Set the pitch in semitone (half-step) intervals. Value between -14 and 14 |
| pitchOctaves |  ``` Optional ```  | Set the pitch in octave intervals.. Value between -1 and 1 |
| pitch |  ``` Optional ```  | Set the pitch (lowness/highness) of the audio. The higher the value, the higher the pitch. Value greater than 0 |
| rate |  ``` Optional ```  | Set the rate for audio. The lower the value, the lower the rate. value greater than 0 |
| tempo |  ``` Optional ```  | Set the tempo (speed) of the audio. A higher value denotes a faster tempo. Value greater than 0 |



#### Example Usage

```python
collect = {}

call_sid = 'CallSid'
collect['call_sid'] = call_sid

audio_direction = AudioDirectionEnum.IN
collect['audio_direction'] = audio_direction

pitch_semi_tones = 46.2043420021442
collect['pitch_semi_tones'] = pitch_semi_tones

pitch_octaves = 46.2043420021442
collect['pitch_octaves'] = pitch_octaves

pitch = 46.2043420021442
collect['pitch'] = pitch

rate = 46.2043420021442
collect['rate'] = rate

tempo = 46.2043420021442
collect['tempo'] = tempo


result = call_controller.create_calls_voiceeffect(collect)

```


### <a name="create_calls_groupcall"></a>![Method: ](https://apidocs.io/img/method.png ".CallController.create_calls_groupcall") create_calls_groupcall

> Group Call

```python
def create_calls_groupcall(self,
                               options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| mfrom |  ``` Required ```  | This number to display on Caller ID as calling |
| to |  ``` Required ```  | Please enter multiple E164 number. You can add max 10 numbers. Add numbers separated with comma. e.g : 1111111111,2222222222 |
| url |  ``` Required ```  | URL requested once the call connects |
| groupConfirmKey |  ``` Required ```  | Define the DTMF that the called party should send to bridge the call. Allowed Values : 0-9, #, * |
| groupConfirmFile |  ``` Required ```  | Specify the audio file you want to play when the called party picks up the call |
| method |  ``` Optional ```  | Specifies the HTTP method used to request the required URL once call connects. |
| statusCallBackUrl |  ``` Optional ```  | URL that can be requested to receive notification when call has ended. A set of default parameters will be sent here once the call is finished. |
| statusCallBackMethod |  ``` Optional ```  | Specifies the HTTP methodlinkclass used to request StatusCallbackUrl. |
| fallBackUrl |  ``` Optional ```  | URL requested if the initial Url parameter fails or encounters an error |
| fallBackMethod |  ``` Optional ```  | Specifies the HTTP method used to request the required FallbackUrl once call connects. |
| heartBeatUrl |  ``` Optional ```  | URL that can be requested every 60 seconds during the call to notify of elapsed time and pass other general information. |
| heartBeatMethod |  ``` Optional ```  | Specifies the HTTP method used to request HeartbeatUrl. |
| timeout |  ``` Optional ```  | Time (in seconds) we should wait while the call is ringing before canceling the call |
| playDtmf |  ``` Optional ```  | DTMF Digits to play to the call once it connects. 0-9, #, or * |
| hideCallerId |  ``` Optional ```  | Specifies if the caller id will be hidden |
| record |  ``` Optional ```  | Specifies if the call should be recorded |
| recordCallBackUrl |  ``` Optional ```  | Recording parameters will be sent here upon completion |
| recordCallBackMethod |  ``` Optional ```  | Method used to request the RecordCallback URL. |
| transcribe |  ``` Optional ```  | Specifies if the call recording should be transcribed |
| transcribeCallBackUrl |  ``` Optional ```  | Transcription parameters will be sent here upon completion |



#### Example Usage

```python
collect = {}

mfrom = 'From'
collect['mfrom'] = mfrom

to = 'To'
collect['to'] = to

url = 'Url'
collect['url'] = url

group_confirm_key = 'GroupConfirmKey'
collect['group_confirm_key'] = group_confirm_key

group_confirm_file = GroupConfirmFileEnum.MP3
collect['group_confirm_file'] = group_confirm_file

method = 'Method'
collect['method'] = method

status_call_back_url = 'StatusCallBackUrl'
collect['status_call_back_url'] = status_call_back_url

status_call_back_method = 'StatusCallBackMethod'
collect['status_call_back_method'] = status_call_back_method

fall_back_url = 'FallBackUrl'
collect['fall_back_url'] = fall_back_url

fall_back_method = 'FallBackMethod'
collect['fall_back_method'] = fall_back_method

heart_beat_url = 'HeartBeatUrl'
collect['heart_beat_url'] = heart_beat_url

heart_beat_method = 'HeartBeatMethod'
collect['heart_beat_method'] = heart_beat_method

timeout = 46
collect['timeout'] = timeout

play_dtmf = 'PlayDtmf'
collect['play_dtmf'] = play_dtmf

hide_caller_id = 'HideCallerId'
collect['hide_caller_id'] = hide_caller_id

record = False
collect['record'] = record

record_call_back_url = 'RecordCallBackUrl'
collect['record_call_back_url'] = record_call_back_url

record_call_back_method = 'RecordCallBackMethod'
collect['record_call_back_method'] = record_call_back_method

transcribe = False
collect['transcribe'] = transcribe

transcribe_call_back_url = 'TranscribeCallBackUrl'
collect['transcribe_call_back_url'] = transcribe_call_back_url


result = call_controller.create_calls_groupcall(collect)

```


### <a name="create_calls_makecall"></a>![Method: ](https://apidocs.io/img/method.png ".CallController.create_calls_makecall") create_calls_makecall

> You can experiment with initiating a call through Ytel and view the request response generated when doing so and get the response in json

```python
def create_calls_makecall(self,
                              options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| mfrom |  ``` Required ```  | A valid Ytel Voice enabled number (E.164 format) that will be initiating the phone call. |
| to |  ``` Required ```  | To number |
| url |  ``` Required ```  | URL requested once the call connects |
| method |  ``` Optional ```  | Specifies the HTTP method used to request the required URL once call connects. |
| statusCallBackUrl |  ``` Optional ```  | URL that can be requested to receive notification when call has ended. A set of default parameters will be sent here once the call is finished. |
| statusCallBackMethod |  ``` Optional ```  | Specifies the HTTP methodlinkclass used to request StatusCallbackUrl. |
| fallBackUrl |  ``` Optional ```  | URL requested if the initial Url parameter fails or encounters an error |
| fallBackMethod |  ``` Optional ```  | Specifies the HTTP method used to request the required FallbackUrl once call connects. |
| heartBeatUrl |  ``` Optional ```  | URL that can be requested every 60 seconds during the call to notify of elapsed tim |
| heartBeatMethod |  ``` Optional ```  | Specifies the HTTP method used to request HeartbeatUrl. |
| timeout |  ``` Optional ```  | Time (in seconds) Ytel should wait while the call is ringing before canceling the call |
| playDtmf |  ``` Optional ```  | DTMF Digits to play to the call once it connects. 0-9, #, or * |
| hideCallerId |  ``` Optional ```  | Specifies if the caller id will be hidden |
| record |  ``` Optional ```  | Specifies if the call should be recorded |
| recordCallBackUrl |  ``` Optional ```  | Recording parameters will be sent here upon completion |
| recordCallBackMethod |  ``` Optional ```  | Method used to request the RecordCallback URL. |
| transcribe |  ``` Optional ```  | Specifies if the call recording should be transcribed |
| transcribeCallBackUrl |  ``` Optional ```  | Transcription parameters will be sent here upon completion |
| ifMachine |  ``` Optional ```  | How Ytel should handle the receiving numbers voicemail machine |
| ifMachineUrl |  ``` Optional ```  | URL requested when IfMachine=continue |
| ifMachineMethod |  ``` Optional ```  | Method used to request the IfMachineUrl. |
| feedback |  ``` Optional ```  | Specify if survey should be enable or not |
| surveyId |  ``` Optional ```  | The unique identifier for the survey. |



#### Example Usage

```python
collect = {}

mfrom = 'From'
collect['mfrom'] = mfrom

to = 'To'
collect['to'] = to

url = 'Url'
collect['url'] = url

method = 'Method'
collect['method'] = method

status_call_back_url = 'StatusCallBackUrl'
collect['status_call_back_url'] = status_call_back_url

status_call_back_method = 'StatusCallBackMethod'
collect['status_call_back_method'] = status_call_back_method

fall_back_url = 'FallBackUrl'
collect['fall_back_url'] = fall_back_url

fall_back_method = 'FallBackMethod'
collect['fall_back_method'] = fall_back_method

heart_beat_url = 'HeartBeatUrl'
collect['heart_beat_url'] = heart_beat_url

heart_beat_method = 'HeartBeatMethod'
collect['heart_beat_method'] = heart_beat_method

timeout = 46
collect['timeout'] = timeout

play_dtmf = 'PlayDtmf'
collect['play_dtmf'] = play_dtmf

hide_caller_id = False
collect['hide_caller_id'] = hide_caller_id

record = False
collect['record'] = record

record_call_back_url = 'RecordCallBackUrl'
collect['record_call_back_url'] = record_call_back_url

record_call_back_method = 'RecordCallBackMethod'
collect['record_call_back_method'] = record_call_back_method

transcribe = False
collect['transcribe'] = transcribe

transcribe_call_back_url = 'TranscribeCallBackUrl'
collect['transcribe_call_back_url'] = transcribe_call_back_url

if_machine = IfMachineEnum.CONTINUE
collect['if_machine'] = if_machine

if_machine_url = 'IfMachineUrl'
collect['if_machine_url'] = if_machine_url

if_machine_method = 'IfMachineMethod'
collect['if_machine_method'] = if_machine_method

feedback = False
collect['feedback'] = feedback

survey_id = 'SurveyId'
collect['survey_id'] = survey_id


result = call_controller.create_calls_makecall(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="phone_number_controller"></a>![Class: ](https://apidocs.io/img/class.png ".PhoneNumberController") PhoneNumberController

### Get controller instance

An instance of the ``` PhoneNumberController ``` class can be accessed from the API Client.

```python
 phone_number_controller = client.phone_number
```

### <a name="create_incomingphone_getdidscore"></a>![Method: ](https://apidocs.io/img/method.png ".PhoneNumberController.create_incomingphone_getdidscore") create_incomingphone_getdidscore

> Get DID Score Number

```python
def create_incomingphone_getdidscore(self,
                                         phonenumber)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phonenumber |  ``` Required ```  | Specifies the multiple phone numbers for check updated spamscore . |



#### Example Usage

```python
phonenumber = 'Phonenumber'

result = phone_number_controller.create_incomingphone_getdidscore(phonenumber)

```


### <a name="create_incomingphone_bulkbuy"></a>![Method: ](https://apidocs.io/img/method.png ".PhoneNumberController.create_incomingphone_bulkbuy") create_incomingphone_bulkbuy

> Purchase a selected number of DID's from specific area codes to be used with your Ytel account.

```python
def create_incomingphone_bulkbuy(self,
                                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| numberType |  ``` Required ```  | The capability the number supports. |
| areaCode |  ``` Required ```  | Specifies the area code for the returned list of available numbers. Only available for North American numbers. |
| quantity |  ``` Required ```  | A positive integer that tells how many number you want to buy at a time. |
| leftover |  ``` Optional ```  | If desired quantity is unavailable purchase what is available . |



#### Example Usage

```python
collect = {}

number_type = Numbertype16Enum.ALL
collect['number_type'] = number_type

area_code = 'AreaCode'
collect['area_code'] = area_code

quantity = 'Quantity'
collect['quantity'] = quantity

leftover = 'Leftover'
collect['leftover'] = leftover


result = phone_number_controller.create_incomingphone_bulkbuy(collect)

```


### <a name="create_incomingphone_listnumber"></a>![Method: ](https://apidocs.io/img/method.png ".PhoneNumberController.create_incomingphone_listnumber") create_incomingphone_listnumber

> Retrieve a list of purchased phones numbers associated with your Ytel account.

```python
def create_incomingphone_listnumber(self,
                                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  ``` DefaultValue ```  | Which page of the overall response will be returned. Page indexing starts at 1. |
| pageSize |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| numberType |  ``` Optional ```  | The capability supported by the number.Number type either SMS,Voice or all |
| friendlyName |  ``` Optional ```  | A human-readable label added to the number object. |



#### Example Usage

```python
collect = {}

page = 1
collect['page'] = page

page_size = 10
collect['page_size'] = page_size

number_type = Numbertype16Enum.ALL
collect['number_type'] = number_type

friendly_name = 'FriendlyName'
collect['friendly_name'] = friendly_name


result = phone_number_controller.create_incomingphone_listnumber(collect)

```


### <a name="create_incomingphone_buynumber"></a>![Method: ](https://apidocs.io/img/method.png ".PhoneNumberController.create_incomingphone_buynumber") create_incomingphone_buynumber

> Purchase a phone number to be used with your Ytel account

```python
def create_incomingphone_buynumber(self,
                                       phone_number)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phoneNumber |  ``` Required ```  | A valid 10-digit Ytel number (E.164 format). |



#### Example Usage

```python
phone_number = 'PhoneNumber'

result = phone_number_controller.create_incomingphone_buynumber(phone_number)

```


### <a name="create_incomingphone_releasenumber_by_response_type_post"></a>![Method: ](https://apidocs.io/img/method.png ".PhoneNumberController.create_incomingphone_releasenumber_by_response_type_post") create_incomingphone_releasenumber_by_response_type_post

> Remove a purchased Ytel number from your account.

```python
def create_incomingphone_releasenumber_by_response_type_post(self,
                                                                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phoneNumber |  ``` Required ```  | A valid 10-digit Ytel number (E.164 format). |
| responseType |  ``` Required ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

phone_number = 'PhoneNumber'
collect['phone_number'] = phone_number

response_type = 'ResponseType'
collect['response_type'] = response_type


result = phone_number_controller.create_incomingphone_releasenumber_by_response_type_post(collect)

```


### <a name="create_incomingphone_viewnumber"></a>![Method: ](https://apidocs.io/img/method.png ".PhoneNumberController.create_incomingphone_viewnumber") create_incomingphone_viewnumber

> Retrieve the details for a phone number by its number.

```python
def create_incomingphone_viewnumber(self,
                                        phone_number)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phoneNumber |  ``` Required ```  | A valid Ytel 10-digit phone number (E.164 format). |



#### Example Usage

```python
phone_number = 'PhoneNumber'

result = phone_number_controller.create_incomingphone_viewnumber(phone_number)

```


### <a name="create_incomingphone_transferphonenumbers"></a>![Method: ](https://apidocs.io/img/method.png ".PhoneNumberController.create_incomingphone_transferphonenumbers") create_incomingphone_transferphonenumbers

> Transfer phone number that has been purchased for from one account to another account.

```python
def create_incomingphone_transferphonenumbers(self,
                                                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phonenumber |  ``` Required ```  | A valid 10-digit Ytel number (E.164 format). |
| fromaccountsid |  ``` Required ```  | A specific Accountsid from where Number is getting transfer. |
| toaccountsid |  ``` Required ```  | A specific Accountsid to which Number is getting transfer. |



#### Example Usage

```python
collect = {}

phonenumber = 'phonenumber'
collect['phonenumber'] = phonenumber

fromaccountsid = 'fromaccountsid'
collect['fromaccountsid'] = fromaccountsid

toaccountsid = 'toaccountsid'
collect['toaccountsid'] = toaccountsid


result = phone_number_controller.create_incomingphone_transferphonenumbers(collect)

```


### <a name="create_incomingphone_massreleasenumber"></a>![Method: ](https://apidocs.io/img/method.png ".PhoneNumberController.create_incomingphone_massreleasenumber") create_incomingphone_massreleasenumber

> Remove a purchased Ytel number from your account.

```python
def create_incomingphone_massreleasenumber(self,
                                               phone_number)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phoneNumber |  ``` Required ```  | A valid Ytel comma separated numbers (E.164 format). |



#### Example Usage

```python
phone_number = 'PhoneNumber'

result = phone_number_controller.create_incomingphone_massreleasenumber(phone_number)

```


### <a name="create_incomingphone_massupdatenumber"></a>![Method: ](https://apidocs.io/img/method.png ".PhoneNumberController.create_incomingphone_massupdatenumber") create_incomingphone_massupdatenumber

> Update properties for a Ytel numbers that has been purchased for your account. Refer to the parameters list for the list of properties that can be updated.

```python
def create_incomingphone_massupdatenumber(self,
                                              options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phoneNumber |  ``` Required ```  | A valid comma(,) separated Ytel numbers. (E.164 format). |
| voiceUrl |  ``` Required ```  | The URL returning InboundXML incoming calls should execute when connected. |
| friendlyName |  ``` Optional ```  | A human-readable value for labeling the number. |
| voiceMethod |  ``` Optional ```  | Specifies the HTTP method used to request the VoiceUrl once incoming call connects. |
| voiceFallbackUrl |  ``` Optional ```  | URL used if any errors occur during execution of InboundXML on a call or at initial request of the voice url |
| voiceFallbackMethod |  ``` Optional ```  | Specifies the HTTP method used to request the VoiceFallbackUrl once incoming call connects. |
| hangupCallback |  ``` Optional ```  | URL that can be requested to receive notification when and how incoming call has ended. |
| hangupCallbackMethod |  ``` Optional ```  | The HTTP method Ytel will use when requesting the HangupCallback URL. |
| heartbeatUrl |  ``` Optional ```  | URL that can be used to monitor the phone number. |
| heartbeatMethod |  ``` Optional ```  | The HTTP method Ytel will use when requesting the HeartbeatUrl. |
| smsUrl |  ``` Optional ```  | URL requested when an SMS is received. |
| smsMethod |  ``` Optional ```  | The HTTP method Ytel will use when requesting the SmsUrl. |
| smsFallbackUrl |  ``` Optional ```  | URL used if any errors occur during execution of InboundXML from an SMS or at initial request of the SmsUrl. |
| smsFallbackMethod |  ``` Optional ```  | The HTTP method Ytel will use when URL requested if the SmsUrl is not available. |



#### Example Usage

```python
collect = {}

phone_number = 'PhoneNumber'
collect['phone_number'] = phone_number

voice_url = 'VoiceUrl'
collect['voice_url'] = voice_url

friendly_name = 'FriendlyName'
collect['friendly_name'] = friendly_name

voice_method = 'VoiceMethod'
collect['voice_method'] = voice_method

voice_fallback_url = 'VoiceFallbackUrl'
collect['voice_fallback_url'] = voice_fallback_url

voice_fallback_method = 'VoiceFallbackMethod'
collect['voice_fallback_method'] = voice_fallback_method

hangup_callback = 'HangupCallback'
collect['hangup_callback'] = hangup_callback

hangup_callback_method = 'HangupCallbackMethod'
collect['hangup_callback_method'] = hangup_callback_method

heartbeat_url = 'HeartbeatUrl'
collect['heartbeat_url'] = heartbeat_url

heartbeat_method = 'HeartbeatMethod'
collect['heartbeat_method'] = heartbeat_method

sms_url = 'SmsUrl'
collect['sms_url'] = sms_url

sms_method = 'SmsMethod'
collect['sms_method'] = sms_method

sms_fallback_url = 'SmsFallbackUrl'
collect['sms_fallback_url'] = sms_fallback_url

sms_fallback_method = 'SmsFallbackMethod'
collect['sms_fallback_method'] = sms_fallback_method


result = phone_number_controller.create_incomingphone_massupdatenumber(collect)

```


### <a name="create_incomingphone_updatenumber"></a>![Method: ](https://apidocs.io/img/method.png ".PhoneNumberController.create_incomingphone_updatenumber") create_incomingphone_updatenumber

> Update properties for a Ytel number that has been purchased for your account. Refer to the parameters list for the list of properties that can be updated.

```python
def create_incomingphone_updatenumber(self,
                                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phoneNumber |  ``` Required ```  | A valid Ytel number (E.164 format). |
| voiceUrl |  ``` Required ```  | URL requested once the call connects |
| friendlyName |  ``` Optional ```  | Phone number friendly name description |
| voiceMethod |  ``` Optional ```  | Post or Get |
| voiceFallbackUrl |  ``` Optional ```  | URL requested if the voice URL is not available |
| voiceFallbackMethod |  ``` Optional ```  | Post or Get |
| hangupCallback |  ``` Optional ```  | callback url after a hangup occurs |
| hangupCallbackMethod |  ``` Optional ```  | Post or Get |
| heartbeatUrl |  ``` Optional ```  | URL requested once the call connects |
| heartbeatMethod |  ``` Optional ```  | URL that can be requested every 60 seconds during the call to notify of elapsed time |
| smsUrl |  ``` Optional ```  | URL requested when an SMS is received |
| smsMethod |  ``` Optional ```  | Post or Get |
| smsFallbackUrl |  ``` Optional ```  | URL used if any errors occur during execution of InboundXML from an SMS or at initial request of the SmsUrl. |
| smsFallbackMethod |  ``` Optional ```  | The HTTP method Ytel will use when URL requested if the SmsUrl is not available. |



#### Example Usage

```python
collect = {}

phone_number = 'PhoneNumber'
collect['phone_number'] = phone_number

voice_url = 'VoiceUrl'
collect['voice_url'] = voice_url

friendly_name = 'FriendlyName'
collect['friendly_name'] = friendly_name

voice_method = 'VoiceMethod'
collect['voice_method'] = voice_method

voice_fallback_url = 'VoiceFallbackUrl'
collect['voice_fallback_url'] = voice_fallback_url

voice_fallback_method = 'VoiceFallbackMethod'
collect['voice_fallback_method'] = voice_fallback_method

hangup_callback = 'HangupCallback'
collect['hangup_callback'] = hangup_callback

hangup_callback_method = 'HangupCallbackMethod'
collect['hangup_callback_method'] = hangup_callback_method

heartbeat_url = 'HeartbeatUrl'
collect['heartbeat_url'] = heartbeat_url

heartbeat_method = 'HeartbeatMethod'
collect['heartbeat_method'] = heartbeat_method

sms_url = 'SmsUrl'
collect['sms_url'] = sms_url

sms_method = 'SmsMethod'
collect['sms_method'] = sms_method

sms_fallback_url = 'SmsFallbackUrl'
collect['sms_fallback_url'] = sms_fallback_url

sms_fallback_method = 'SmsFallbackMethod'
collect['sms_fallback_method'] = sms_fallback_method


result = phone_number_controller.create_incomingphone_updatenumber(collect)

```


### <a name="create_incomingphone_availablenumber"></a>![Method: ](https://apidocs.io/img/method.png ".PhoneNumberController.create_incomingphone_availablenumber") create_incomingphone_availablenumber

> Retrieve a list of available phone numbers that can be purchased and used for your Ytel account.

```python
def create_incomingphone_availablenumber(self,
                                             options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| numbertype |  ``` Required ```  | Number type either SMS,Voice or all |
| areacode |  ``` Required ```  | Specifies the area code for the returned list of available numbers. Only available for North American numbers. |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | The count of objects to return. |



#### Example Usage

```python
collect = {}

numbertype = Numbertype16Enum.ALL
collect['numbertype'] = numbertype

areacode = 'areacode'
collect['areacode'] = areacode

pagesize = 10
collect['pagesize'] = pagesize


result = phone_number_controller.create_incomingphone_availablenumber(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="sms_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SMSController") SMSController

### Get controller instance

An instance of the ``` SMSController ``` class can be accessed from the API Client.

```python
 sms_controller = client.sms
```

### <a name="create_sms_viewdetailsms"></a>![Method: ](https://apidocs.io/img/method.png ".SMSController.create_sms_viewdetailsms") create_sms_viewdetailsms

> Retrieve a single SMS message object with details by its SmsSid.

```python
def create_sms_viewdetailsms(self,
                                 message_sid)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| messageSid |  ``` Required ```  | The unique identifier for a sms message. |



#### Example Usage

```python
message_sid = 'MessageSid'

result = sms_controller.create_sms_viewdetailsms(message_sid)

```


### <a name="create_sms_viewsms"></a>![Method: ](https://apidocs.io/img/method.png ".SMSController.create_sms_viewsms") create_sms_viewsms

> Retrieve a single SMS message object by its SmsSid.

```python
def create_sms_viewsms(self,
                           message_sid)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| messageSid |  ``` Required ```  | The unique identifier for a sms message. |



#### Example Usage

```python
message_sid = 'MessageSid'

result = sms_controller.create_sms_viewsms(message_sid)

```


### <a name="create_sms_getinboundsms"></a>![Method: ](https://apidocs.io/img/method.png ".SMSController.create_sms_getinboundsms") create_sms_getinboundsms

> Retrieve a list of Inbound SMS message objects.

```python
def create_sms_getinboundsms(self,
                                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pageSize |  ``` Optional ```  ``` DefaultValue ```  | The count of objects to return per page. |
| mfrom |  ``` Optional ```  | Filter SMS message objects from this valid 10-digit phone number (E.164 format). |
| to |  ``` Optional ```  | Filter SMS message objects to this valid 10-digit phone number (E.164 format). |
| dateSent |  ``` Optional ```  | Filter sms message objects by this date. |



#### Example Usage

```python
collect = {}

page = 1
collect['page'] = page

page_size = 10
collect['page_size'] = page_size

mfrom = 'From'
collect['mfrom'] = mfrom

to = 'To'
collect['to'] = to

date_sent = 'DateSent'
collect['date_sent'] = date_sent


result = sms_controller.create_sms_getinboundsms(collect)

```


### <a name="create_sms_listsms"></a>![Method: ](https://apidocs.io/img/method.png ".SMSController.create_sms_listsms") create_sms_listsms

> Retrieve a list of Outbound SMS message objects.

```python
def create_sms_listsms(self,
                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pageSize |  ``` Optional ```  ``` DefaultValue ```  | Number of individual resources listed in the response per page |
| mfrom |  ``` Optional ```  | Filter SMS message objects from this valid 10-digit phone number (E.164 format). |
| to |  ``` Optional ```  | Filter SMS message objects to this valid 10-digit phone number (E.164 format). |
| dateSent |  ``` Optional ```  | Only list SMS messages sent in the specified date range |



#### Example Usage

```python
collect = {}

page = 1
collect['page'] = page

page_size = 10
collect['page_size'] = page_size

mfrom = 'From'
collect['mfrom'] = mfrom

to = 'To'
collect['to'] = to

date_sent = 'DateSent'
collect['date_sent'] = date_sent


result = sms_controller.create_sms_listsms(collect)

```


### <a name="create_sms_sendsms"></a>![Method: ](https://apidocs.io/img/method.png ".SMSController.create_sms_sendsms") create_sms_sendsms

> Send an SMS from a Ytel number

```python
def create_sms_sendsms(self,
                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| mfrom |  ``` Required ```  | The 10-digit SMS-enabled Ytel number (E.164 format) in which the message is sent. |
| to |  ``` Required ```  | The 10-digit phone number (E.164 format) that will receive the message. |
| body |  ``` Required ```  | The body message that is to be sent in the text. |
| method |  ``` Optional ```  | Specifies the HTTP method used to request the required URL once SMS sent. |
| messageStatusCallback |  ``` Optional ```  | URL that can be requested to receive notification when SMS has Sent. A set of default parameters will be sent here once the SMS is finished. |
| smartsms |  ``` Optional ```  ``` DefaultValue ```  | Check's 'to' number can receive sms or not using Carrier API, if wireless = true then text sms is sent, else wireless = false then call is recieved to end user with audible message. |
| deliveryStatus |  ``` Optional ```  ``` DefaultValue ```  | Delivery reports are a method to tell your system if the message has arrived on the destination phone. |



#### Example Usage

```python
collect = {}

mfrom = 'From'
collect['mfrom'] = mfrom

to = 'To'
collect['to'] = to

body = 'Body'
collect['body'] = body

method = 'Method'
collect['method'] = method

message_status_callback = 'MessageStatusCallback'
collect['message_status_callback'] = message_status_callback

smartsms = False
collect['smartsms'] = smartsms

delivery_status = False
collect['delivery_status'] = delivery_status


result = sms_controller.create_sms_sendsms(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="shared_short_code_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SharedShortCodeController") SharedShortCodeController

### Get controller instance

An instance of the ``` SharedShortCodeController ``` class can be accessed from the API Client.

```python
 shared_short_code_controller = client.shared_short_code
```

### <a name="create_shortcode_viewshortcode"></a>![Method: ](https://apidocs.io/img/method.png ".SharedShortCodeController.create_shortcode_viewshortcode") create_shortcode_viewshortcode

> The response returned here contains all resource properties associated with the given Shortcode.

```python
def create_shortcode_viewshortcode(self,
                                       shortcode)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| shortcode |  ``` Required ```  | List of valid Shortcode to your Ytel account |



#### Example Usage

```python
shortcode = 'Shortcode'

result = shared_short_code_controller.create_shortcode_viewshortcode(shortcode)

```


### <a name="create_keyword_view"></a>![Method: ](https://apidocs.io/img/method.png ".SharedShortCodeController.create_keyword_view") create_keyword_view

> View a set of properties for a single keyword.

```python
def create_keyword_view(self,
                            keywordid)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| keywordid |  ``` Required ```  | The unique identifier of each keyword |



#### Example Usage

```python
keywordid = 'Keywordid'

result = shared_short_code_controller.create_keyword_view(keywordid)

```


### <a name="create_shortcode_updateshortcode"></a>![Method: ](https://apidocs.io/img/method.png ".SharedShortCodeController.create_shortcode_updateshortcode") create_shortcode_updateshortcode

> Update Assignment

```python
def create_shortcode_updateshortcode(self,
                                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| shortcode |  ``` Required ```  | List of valid shortcode to your Ytel account |
| friendlyName |  ``` Optional ```  | User generated name of the shortcode |
| callbackUrl |  ``` Optional ```  | URL that can be requested to receive notification when call has ended. A set of default parameters will be sent here once the call is finished. |
| callbackMethod |  ``` Optional ```  | Specifies the HTTP method used to request the required StatusCallBackUrl once call connects. |
| fallbackUrl |  ``` Optional ```  | URL used if any errors occur during execution of InboundXML or at initial request of the required Url provided with the POST. |
| fallbackUrlMethod |  ``` Optional ```  | Specifies the HTTP method used to request the required FallbackUrl once call connects. |



#### Example Usage

```python
collect = {}

shortcode = 'Shortcode'
collect['shortcode'] = shortcode

friendly_name = 'FriendlyName'
collect['friendly_name'] = friendly_name

callback_url = 'CallbackUrl'
collect['callback_url'] = callback_url

callback_method = 'CallbackMethod'
collect['callback_method'] = callback_method

fallback_url = 'FallbackUrl'
collect['fallback_url'] = fallback_url

fallback_url_method = 'FallbackUrlMethod'
collect['fallback_url_method'] = fallback_url_method


result = shared_short_code_controller.create_shortcode_updateshortcode(collect)

```


### <a name="create_template_view"></a>![Method: ](https://apidocs.io/img/method.png ".SharedShortCodeController.create_template_view") create_template_view

> View a Shared ShortCode Template

```python
def create_template_view(self,
                             template_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| templateId |  ``` Required ```  | The unique identifier for a template object |



#### Example Usage

```python
template_id = uuid.uuid4()

result = shared_short_code_controller.create_template_view(template_id)

```


### <a name="create_shortcode_listshortcode"></a>![Method: ](https://apidocs.io/img/method.png ".SharedShortCodeController.create_shortcode_listshortcode") create_shortcode_listshortcode

> Retrieve a list of shortcode assignment associated with your Ytel account.

```python
def create_shortcode_listshortcode(self,
                                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | Number of individual resources listed in the response per page |
| shortcode |  ``` Optional ```  | Only list keywords of shortcode |



#### Example Usage

```python
collect = {}

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize

shortcode = 'Shortcode'
collect['shortcode'] = shortcode


result = shared_short_code_controller.create_shortcode_listshortcode(collect)

```


### <a name="create_keyword_lists"></a>![Method: ](https://apidocs.io/img/method.png ".SharedShortCodeController.create_keyword_lists") create_keyword_lists

> Retrieve a list of keywords associated with your Ytel account.

```python
def create_keyword_lists(self,
                             options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | Number of individual resources listed in the response per page |
| keyword |  ``` Optional ```  | Only list keywords of keyword |
| shortcode |  ``` Optional ```  | Only list keywords of shortcode |



#### Example Usage

```python
collect = {}

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize

keyword = 'Keyword'
collect['keyword'] = keyword

shortcode = 4
collect['shortcode'] = shortcode


result = shared_short_code_controller.create_keyword_lists(collect)

```


### <a name="create_template_lists"></a>![Method: ](https://apidocs.io/img/method.png ".SharedShortCodeController.create_template_lists") create_template_lists

> List Shortcode Templates by Type

```python
def create_template_lists(self,
                              options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| mtype |  ``` Optional ```  ``` DefaultValue ```  | The type (category) of template Valid values: marketing, authorization |
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | The count of objects to return per page. |
| shortcode |  ``` Optional ```  | Only list templates of type |



#### Example Usage

```python
collect = {}

mtype = 'authorization'
collect['mtype'] = mtype

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize

shortcode = 'Shortcode'
collect['shortcode'] = shortcode


result = shared_short_code_controller.create_template_lists(collect)

```


### <a name="create_shortcode_sendsms"></a>![Method: ](https://apidocs.io/img/method.png ".SharedShortCodeController.create_shortcode_sendsms") create_shortcode_sendsms

> Send an SMS from a Ytel ShortCode

```python
def create_shortcode_sendsms(self,
                                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| shortcode |  ``` Required ```  | The Short Code number that is the sender of this message |
| to |  ``` Required ```  | A valid 10-digit number that should receive the message |
| templateid |  ``` Required ```  | The unique identifier for the template used for the message |
| data |  ``` Required ```  | format of your data, example: {companyname}:test,{otpcode}:1234 |
| method |  ``` Optional ```  ``` DefaultValue ```  | Specifies the HTTP method used to request the required URL once the Short Code message is sent. |
| messageStatusCallback |  ``` Optional ```  | URL that can be requested to receive notification when Short Code message was sent. |



#### Example Usage

```python
collect = {}

shortcode = 'shortcode'
collect['shortcode'] = shortcode

to = 'to'
collect['to'] = to

templateid = uuid.uuid4()
collect['templateid'] = templateid

data = 'data'
collect['data'] = data

method = 'GET'
collect['method'] = method

message_status_callback = 'MessageStatusCallback'
collect['message_status_callback'] = message_status_callback


result = shared_short_code_controller.create_shortcode_sendsms(collect)

```


### <a name="create_shortcode_getinboundsms"></a>![Method: ](https://apidocs.io/img/method.png ".SharedShortCodeController.create_shortcode_getinboundsms") create_shortcode_getinboundsms

> List All Inbound ShortCode

```python
def create_shortcode_getinboundsms(self,
                                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | Number of individual resources listed in the response per page |
| mfrom |  ``` Optional ```  | From Number to Inbound ShortCode |
| shortcode |  ``` Optional ```  | Only list messages sent to this Short Code |
| datecreated |  ``` Optional ```  | Only list messages sent with the specified date |



#### Example Usage

```python
collect = {}

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize

mfrom = 'from'
collect['mfrom'] = mfrom

shortcode = 'Shortcode'
collect['shortcode'] = shortcode

datecreated = 'Datecreated'
collect['datecreated'] = datecreated


result = shared_short_code_controller.create_shortcode_getinboundsms(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="conference_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ConferenceController") ConferenceController

### Get controller instance

An instance of the ``` ConferenceController ``` class can be accessed from the API Client.

```python
 conference_controller = client.conference
```

### <a name="create_conferences_play_audio"></a>![Method: ](https://apidocs.io/img/method.png ".ConferenceController.create_conferences_play_audio") create_conferences_play_audio

> Play an audio file during a conference.

```python
def create_conferences_play_audio(self,
                                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| conferenceSid |  ``` Required ```  | The unique identifier for a conference object. |
| participantSid |  ``` Required ```  | The unique identifier for a participant object. |
| audioUrl |  ``` Required ```  | The URL for the audio file that is to be played during the conference. Multiple audio files can be chained by using a semicolon. |



#### Example Usage

```python
collect = {}

conference_sid = 'ConferenceSid'
collect['conference_sid'] = conference_sid

participant_sid = 'ParticipantSid'
collect['participant_sid'] = participant_sid

audio_url = AudioUrlEnum.MP3
collect['audio_url'] = audio_url


result = conference_controller.create_conferences_play_audio(collect)

```


### <a name="create_conferences_hangup_participant"></a>![Method: ](https://apidocs.io/img/method.png ".ConferenceController.create_conferences_hangup_participant") create_conferences_hangup_participant

> Remove a participant from a conference.

```python
def create_conferences_hangup_participant(self,
                                              options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| conferenceSid |  ``` Required ```  | The unique identifier for a conference object. |
| participantSid |  ``` Required ```  | The unique identifier for a participant object. |



#### Example Usage

```python
collect = {}

conference_sid = 'ConferenceSid'
collect['conference_sid'] = conference_sid

participant_sid = 'ParticipantSid'
collect['participant_sid'] = participant_sid


result = conference_controller.create_conferences_hangup_participant(collect)

```


### <a name="create_conferences_viewconference"></a>![Method: ](https://apidocs.io/img/method.png ".ConferenceController.create_conferences_viewconference") create_conferences_viewconference

> Retrieve information about a conference by its ConferenceSid.

```python
def create_conferences_viewconference(self,
                                          conference_sid)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| conferenceSid |  ``` Required ```  | The unique identifier of each conference resource |



#### Example Usage

```python
conference_sid = 'ConferenceSid'

result = conference_controller.create_conferences_viewconference(conference_sid)

```


### <a name="create_conferences_listconference"></a>![Method: ](https://apidocs.io/img/method.png ".ConferenceController.create_conferences_listconference") create_conferences_listconference

> Retrieve a list of conference objects.

```python
def create_conferences_listconference(self,
                                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | Number of individual resources listed in the response per page |
| friendlyName |  ``` Optional ```  | Only return conferences with the specified FriendlyName |
| dateCreated |  ``` Optional ```  | Conference created date |



#### Example Usage

```python
collect = {}

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize

friendly_name = 'FriendlyName'
collect['friendly_name'] = friendly_name

date_created = 'DateCreated'
collect['date_created'] = date_created


result = conference_controller.create_conferences_listconference(collect)

```


### <a name="create_conferences_list_participant"></a>![Method: ](https://apidocs.io/img/method.png ".ConferenceController.create_conferences_list_participant") create_conferences_list_participant

> Retrieve a list of participants for an in-progress conference.

```python
def create_conferences_list_participant(self,
                                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| conferenceSid |  ``` Required ```  | The unique identifier for a conference. |
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | The count of objects to return per page. |
| muted |  ``` Optional ```  | Specifies if participant should be muted. |
| deaf |  ``` Optional ```  | Specifies if the participant should hear audio in the conference. |



#### Example Usage

```python
collect = {}

conference_sid = 'ConferenceSid'
collect['conference_sid'] = conference_sid

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize

muted = False
collect['muted'] = muted

deaf = False
collect['deaf'] = deaf


result = conference_controller.create_conferences_list_participant(collect)

```


### <a name="create_conferences_view_participant"></a>![Method: ](https://apidocs.io/img/method.png ".ConferenceController.create_conferences_view_participant") create_conferences_view_participant

> Retrieve information about a participant by its ParticipantSid.

```python
def create_conferences_view_participant(self,
                                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| conferenceSid |  ``` Required ```  | The unique identifier for a conference object. |
| participantSid |  ``` Required ```  | The unique identifier for a participant object. |



#### Example Usage

```python
collect = {}

conference_sid = 'ConferenceSid'
collect['conference_sid'] = conference_sid

participant_sid = 'ParticipantSid'
collect['participant_sid'] = participant_sid


result = conference_controller.create_conferences_view_participant(collect)

```


### <a name="create_conferences_add_participant"></a>![Method: ](https://apidocs.io/img/method.png ".ConferenceController.create_conferences_add_participant") create_conferences_add_participant

> Add Participant in conference 

```python
def create_conferences_add_participant(self,
                                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| conferenceSid |  ``` Required ```  | The unique identifier for a conference object. |
| participantNumber |  ``` Required ```  | The phone number of the participant to be added. |
| muted |  ``` Optional ```  | Specifies if participant should be muted. |
| deaf |  ``` Optional ```  | Specifies if the participant should hear audio in the conference. |



#### Example Usage

```python
collect = {}

conference_sid = 'ConferenceSid'
collect['conference_sid'] = conference_sid

participant_number = 'ParticipantNumber'
collect['participant_number'] = participant_number

muted = False
collect['muted'] = muted

deaf = False
collect['deaf'] = deaf


result = conference_controller.create_conferences_add_participant(collect)

```


### <a name="create_conferences_create_conference"></a>![Method: ](https://apidocs.io/img/method.png ".ConferenceController.create_conferences_create_conference") create_conferences_create_conference

> Here you can experiment with initiating a conference call through Ytel and view the request response generated when doing so.

```python
def create_conferences_create_conference(self,
                                             options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| mfrom |  ``` Required ```  | A valid 10-digit number (E.164 format) that will be initiating the conference call. |
| to |  ``` Required ```  | A valid 10-digit number (E.164 format) that is to receive the conference call. |
| url |  ``` Required ```  | URL requested once the conference connects |
| method |  ``` Optional ```  ``` DefaultValue ```  | Specifies the HTTP method used to request the required URL once call connects. |
| statusCallBackUrl |  ``` Optional ```  | URL that can be requested to receive notification when call has ended. A set of default parameters will be sent here once the conference is finished. |
| statusCallBackMethod |  ``` Optional ```  | Specifies the HTTP methodlinkclass used to request StatusCallbackUrl. |
| fallbackUrl |  ``` Optional ```  | URL requested if the initial Url parameter fails or encounters an error |
| fallbackMethod |  ``` Optional ```  | Specifies the HTTP method used to request the required FallbackUrl once call connects. |
| record |  ``` Optional ```  | Specifies if the conference should be recorded. |
| recordCallBackUrl |  ``` Optional ```  | Recording parameters will be sent here upon completion. |
| recordCallBackMethod |  ``` Optional ```  | Specifies the HTTP method used to request the required URL once conference connects. |
| scheduleTime |  ``` Optional ```  | Schedule conference in future. Schedule time must be greater than current time |
| timeout |  ``` Optional ```  | The number of seconds the call stays on the line while waiting for an answer. The max time limit is 999 and the default limit is 60 seconds but lower times can be set. |



#### Example Usage

```python
collect = {}

mfrom = 'From'
collect['mfrom'] = mfrom

to = 'To'
collect['to'] = to

url = 'Url'
collect['url'] = url

method = 'POST'
collect['method'] = method

status_call_back_url = 'StatusCallBackUrl'
collect['status_call_back_url'] = status_call_back_url

status_call_back_method = 'StatusCallBackMethod'
collect['status_call_back_method'] = status_call_back_method

fallback_url = 'FallbackUrl'
collect['fallback_url'] = fallback_url

fallback_method = 'FallbackMethod'
collect['fallback_method'] = fallback_method

record = False
collect['record'] = record

record_call_back_url = 'RecordCallBackUrl'
collect['record_call_back_url'] = record_call_back_url

record_call_back_method = 'RecordCallBackMethod'
collect['record_call_back_method'] = record_call_back_method

schedule_time = 'ScheduleTime'
collect['schedule_time'] = schedule_time

timeout = 95
collect['timeout'] = timeout


result = conference_controller.create_conferences_create_conference(collect)

```


### <a name="create_conferences_deaf_mute_participant"></a>![Method: ](https://apidocs.io/img/method.png ".ConferenceController.create_conferences_deaf_mute_participant") create_conferences_deaf_mute_participant

> Deaf Mute Participant

```python
def create_conferences_deaf_mute_participant(self,
                                                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| conferenceSid |  ``` Required ```  | ID of the active conference |
| participantSid |  ``` Required ```  | ID of an active participant |
| muted |  ``` Optional ```  | Mute a participant |
| deaf |  ``` Optional ```  | Make it so a participant cant hear |



#### Example Usage

```python
collect = {}

conference_sid = 'conferenceSid'
collect['conference_sid'] = conference_sid

participant_sid = 'ParticipantSid'
collect['participant_sid'] = participant_sid

muted = False
collect['muted'] = muted

deaf = False
collect['deaf'] = deaf


result = conference_controller.create_conferences_deaf_mute_participant(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="carrier_controller"></a>![Class: ](https://apidocs.io/img/class.png ".CarrierController") CarrierController

### Get controller instance

An instance of the ``` CarrierController ``` class can be accessed from the API Client.

```python
 carrier_controller = client.carrier
```

### <a name="create_carrier_lookup"></a>![Method: ](https://apidocs.io/img/method.png ".CarrierController.create_carrier_lookup") create_carrier_lookup

> Get the Carrier Lookup

```python
def create_carrier_lookup(self,
                              phone_number)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phoneNumber |  ``` Required ```  | A valid 10-digit number (E.164 format). |



#### Example Usage

```python
phone_number = 'PhoneNumber'

result = carrier_controller.create_carrier_lookup(phone_number)

```


### <a name="create_carrier_lookuplist"></a>![Method: ](https://apidocs.io/img/method.png ".CarrierController.create_carrier_lookuplist") create_carrier_lookuplist

> Retrieve a list of carrier lookup objects.

```python
def create_carrier_lookuplist(self,
                                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pageSize |  ``` Optional ```  ``` DefaultValue ```  | The count of objects to return per page. |



#### Example Usage

```python
collect = {}

page = 1
collect['page'] = page

page_size = 10
collect['page_size'] = page_size


result = carrier_controller.create_carrier_lookuplist(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="email_controller"></a>![Class: ](https://apidocs.io/img/class.png ".EmailController") EmailController

### Get controller instance

An instance of the ``` EmailController ``` class can be accessed from the API Client.

```python
 email_controller = client.email
```

### <a name="create_email_deleteinvalidemail"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.create_email_deleteinvalidemail") create_email_deleteinvalidemail

> Remove an email from the invalid email list.

```python
def create_email_deleteinvalidemail(self,
                                        email)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| email |  ``` Required ```  | A valid email address that is to be remove from the invalid email list. |



#### Example Usage

```python
email = 'Email'

result = email_controller.create_email_deleteinvalidemail(email)

```


### <a name="create_email_listblockemail"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.create_email_listblockemail") create_email_listblockemail

> Retrieve a list of emails that have been blocked.

```python
def create_email_listblockemail(self,
                                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| offset |  ``` Optional ```  | The starting point of the list of blocked emails that should be returned. |
| limit |  ``` Optional ```  | The count of results that should be returned. |



#### Example Usage

```python
collect = {}

offset = 'Offset'
collect['offset'] = offset

limit = 'Limit'
collect['limit'] = limit


result = email_controller.create_email_listblockemail(collect)

```


### <a name="create_email_listspamemail"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.create_email_listspamemail") create_email_listspamemail

> Retrieve a list of emails that are on the spam list.

```python
def create_email_listspamemail(self,
                                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| offset |  ``` Optional ```  | The starting point of the list of spam emails that should be returned. |
| limit |  ``` Optional ```  | The count of results that should be returned. |



#### Example Usage

```python
collect = {}

offset = 'Offset'
collect['offset'] = offset

limit = 'Limit'
collect['limit'] = limit


result = email_controller.create_email_listspamemail(collect)

```


### <a name="create_email_listbounceemail"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.create_email_listbounceemail") create_email_listbounceemail

> Retrieve a list of emails that have bounced.

```python
def create_email_listbounceemail(self,
                                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| offset |  ``` Optional ```  | The starting point of the list of bounced emails that should be returned. |
| limit |  ``` Optional ```  | The count of results that should be returned. |



#### Example Usage

```python
collect = {}

offset = 'Offset'
collect['offset'] = offset

limit = 'Limit'
collect['limit'] = limit


result = email_controller.create_email_listbounceemail(collect)

```


### <a name="create_email_deletebouncesemail"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.create_email_deletebouncesemail") create_email_deletebouncesemail

> Remove an email address from the bounced list.

```python
def create_email_deletebouncesemail(self,
                                        email)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| email |  ``` Required ```  | The email address to be remove from the bounced email list. |



#### Example Usage

```python
email = 'Email'

result = email_controller.create_email_deletebouncesemail(email)

```


### <a name="create_email_listinvalidemail"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.create_email_listinvalidemail") create_email_listinvalidemail

> Retrieve a list of invalid email addresses.

```python
def create_email_listinvalidemail(self,
                                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| offset |  ``` Optional ```  | The starting point of the list of invalid emails that should be returned. |
| limit |  ``` Optional ```  | The count of results that should be returned. |



#### Example Usage

```python
collect = {}

offset = 'Offset'
collect['offset'] = offset

limit = 'Limit'
collect['limit'] = limit


result = email_controller.create_email_listinvalidemail(collect)

```


### <a name="create_email_listunsubscribedemail"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.create_email_listunsubscribedemail") create_email_listunsubscribedemail

> Retrieve a list of email addresses from the unsubscribe list.

```python
def create_email_listunsubscribedemail(self,
                                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| offset |  ``` Optional ```  | The starting point of the list of unsubscribed emails that should be returned. |
| limit |  ``` Optional ```  | The count of results that should be returned. |



#### Example Usage

```python
collect = {}

offset = 'Offset'
collect['offset'] = offset

limit = 'Limit'
collect['limit'] = limit


result = email_controller.create_email_listunsubscribedemail(collect)

```


### <a name="create_email_deleteunsubscribedemail"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.create_email_deleteunsubscribedemail") create_email_deleteunsubscribedemail

> Remove an email address from the list of unsubscribed emails.

```python
def create_email_deleteunsubscribedemail(self,
                                             email)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| email |  ``` Required ```  | A valid email address that is to be remove from the unsubscribe list. |



#### Example Usage

```python
email = 'email'

result = email_controller.create_email_deleteunsubscribedemail(email)

```


### <a name="create_email_addunsubscribesemail"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.create_email_addunsubscribesemail") create_email_addunsubscribesemail

> Add an email to the unsubscribe list

```python
def create_email_addunsubscribesemail(self,
                                          email)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| email |  ``` Required ```  | A valid email address that is to be added to the unsubscribe list |



#### Example Usage

```python
email = 'email'

result = email_controller.create_email_addunsubscribesemail(email)

```


### <a name="create_email_deleteblocksemail"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.create_email_deleteblocksemail") create_email_deleteblocksemail

> Remove an email from blocked emails list.

```python
def create_email_deleteblocksemail(self,
                                       email)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| email |  ``` Required ```  | The email address to be remove from the blocked list. |



#### Example Usage

```python
email = 'Email'

result = email_controller.create_email_deleteblocksemail(email)

```


### <a name="create_email_deletespamemail"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.create_email_deletespamemail") create_email_deletespamemail

> Remove an email from the spam email list.

```python
def create_email_deletespamemail(self,
                                     email)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| email |  ``` Required ```  | A valid email address that is to be remove from the spam list. |



#### Example Usage

```python
email = 'Email'

result = email_controller.create_email_deletespamemail(email)

```


### <a name="create_email_sendemails"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.create_email_sendemails") create_email_sendemails

> Create and submit an email message to one or more email addresses.

```python
def create_email_sendemails(self,
                                options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| to |  ``` Required ```  | A valid address that will receive the email. Multiple addresses can be separated by using commas. |
| mtype |  ``` Required ```  | Specifies the type of email to be sent |
| subject |  ``` Required ```  | The subject of the mail. Must be a valid string. |
| message |  ``` Required ```  | The email message that is to be sent in the text. |
| mfrom |  ``` Optional ```  | A valid address that will send the email. |
| cc |  ``` Optional ```  | Carbon copy. A valid address that will receive the email. Multiple addresses can be separated by using commas. |
| bcc |  ``` Optional ```  | Blind carbon copy. A valid address that will receive the email. Multiple addresses can be separated by using commas. |
| attachment |  ``` Optional ```  | A file that is attached to the email. Must be less than 7 MB in size. |



#### Example Usage

```python
collect = {}

to = 'To'
collect['to'] = to

mtype = TypeEnum.TEXT
collect['mtype'] = mtype

subject = 'Subject'
collect['subject'] = subject

message = 'Message'
collect['message'] = message

mfrom = 'From'
collect['mfrom'] = mfrom

cc = 'Cc'
collect['cc'] = cc

bcc = 'Bcc'
collect['bcc'] = bcc

attachment = 'Attachment'
collect['attachment'] = attachment


result = email_controller.create_email_sendemails(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="account_controller"></a>![Class: ](https://apidocs.io/img/class.png ".AccountController") AccountController

### Get controller instance

An instance of the ``` AccountController ``` class can be accessed from the API Client.

```python
 account_controller = client.account
```

### <a name="create_accounts_viewaccount"></a>![Method: ](https://apidocs.io/img/method.png ".AccountController.create_accounts_viewaccount") create_accounts_viewaccount

> Retrieve information regarding your Ytel account by a specific date. The response object will contain data such as account status, balance, and account usage totals.

```python
def create_accounts_viewaccount(self,
                                    date)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| date |  ``` Required ```  | Filter account information based on date. |



#### Example Usage

```python
date = 'Date'

result = account_controller.create_accounts_viewaccount(date)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="sub_account_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SubAccountController") SubAccountController

### Get controller instance

An instance of the ``` SubAccountController ``` class can be accessed from the API Client.

```python
 sub_account_controller = client.sub_account
```

### <a name="create_user_subaccountactivation"></a>![Method: ](https://apidocs.io/img/method.png ".SubAccountController.create_user_subaccountactivation") create_user_subaccountactivation

> Suspend or unsuspend

```python
def create_user_subaccountactivation(self,
                                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subAccountSID |  ``` Required ```  | The SubaccountSid to be activated or suspended |
| mActivate |  ``` Required ```  | 0 to suspend or 1 to activate |



#### Example Usage

```python
collect = {}

sub_account_sid = 'SubAccountSID'
collect['sub_account_sid'] = sub_account_sid

m_activate = MActivateEnum.ACTIVATE
collect['m_activate'] = m_activate


result = sub_account_controller.create_user_subaccountactivation(collect)

```


### <a name="create_user_deletesubaccount"></a>![Method: ](https://apidocs.io/img/method.png ".SubAccountController.create_user_deletesubaccount") create_user_deletesubaccount

> Delete sub account or merge numbers into parent

```python
def create_user_deletesubaccount(self,
                                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subAccountSID |  ``` Required ```  | The SubaccountSid to be deleted |
| mergeNumber |  ``` Required ```  | 0 to delete or 1 to merge numbers to parent account. |



#### Example Usage

```python
collect = {}

sub_account_sid = 'SubAccountSID'
collect['sub_account_sid'] = sub_account_sid

merge_number = MergeNumberEnum.DELETE
collect['merge_number'] = merge_number


result = sub_account_controller.create_user_deletesubaccount(collect)

```


### <a name="create_user_createsubaccount"></a>![Method: ](https://apidocs.io/img/method.png ".SubAccountController.create_user_createsubaccount") create_user_createsubaccount

> Create a sub user account under the parent account

```python
def create_user_createsubaccount(self,
                                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| firstName |  ``` Required ```  | Sub account user first name |
| lastName |  ``` Required ```  | sub account user last name |
| email |  ``` Required ```  | Sub account email address |
| friendlyName |  ``` Required ```  | Descriptive name of the sub account |
| password |  ``` Required ```  | The password of the sub account.  Please make sure to make as password that is at least 8 characters long, contain a symbol, uppercase and a number. |



#### Example Usage

```python
collect = {}

first_name = 'FirstName'
collect['first_name'] = first_name

last_name = 'LastName'
collect['last_name'] = last_name

email = 'Email'
collect['email'] = email

friendly_name = 'FriendlyName'
collect['friendly_name'] = friendly_name

password = 'Password'
collect['password'] = password


result = sub_account_controller.create_user_createsubaccount(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="address_controller"></a>![Class: ](https://apidocs.io/img/class.png ".AddressController") AddressController

### Get controller instance

An instance of the ``` AddressController ``` class can be accessed from the API Client.

```python
 address_controller = client.address
```

### <a name="address_deleteaddress"></a>![Method: ](https://apidocs.io/img/method.png ".AddressController.address_deleteaddress") address_deleteaddress

> To delete Address to your address book

```python
def address_deleteaddress(self,
                              addressid)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| addressid |  ``` Required ```  | The identifier of the address to be deleted. |



#### Example Usage

```python
addressid = 'addressid'

result = address_controller.address_deleteaddress(addressid)

```


### <a name="address_verifyaddress"></a>![Method: ](https://apidocs.io/img/method.png ".AddressController.address_verifyaddress") address_verifyaddress

> Validates an address given.

```python
def address_verifyaddress(self,
                              addressid)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| addressid |  ``` Required ```  | The identifier of the address to be verified. |



#### Example Usage

```python
addressid = 'addressid'

result = address_controller.address_verifyaddress(addressid)

```


### <a name="address_viewaddress"></a>![Method: ](https://apidocs.io/img/method.png ".AddressController.address_viewaddress") address_viewaddress

> View Address Specific address Book by providing the address id

```python
def address_viewaddress(self,
                            addressid)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| addressid |  ``` Required ```  | The identifier of the address to be retrieved. |



#### Example Usage

```python
addressid = 'addressid'

result = address_controller.address_viewaddress(addressid)

```


### <a name="address_createaddress"></a>![Method: ](https://apidocs.io/img/method.png ".AddressController.address_createaddress") address_createaddress

> To add an address to your address book, you create a new address object. You can retrieve and delete individual addresses as well as get a list of addresses. Addresses are identified by a unique random ID.

```python
def address_createaddress(self,
                              options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| name |  ``` Required ```  | Name of user |
| address |  ``` Required ```  | Address of user. |
| country |  ``` Required ```  | Must be a 2 letter country short-name code (ISO 3166) |
| state |  ``` Required ```  | Must be a 2 letter State eg. CA for US. For Some Countries it can be greater than 2 letters. |
| city |  ``` Required ```  | City Name. |
| zip |  ``` Required ```  | Zip code of city. |
| description |  ``` Optional ```  | Description of addresses. |
| email |  ``` Optional ```  | Email Id of user. |
| phone |  ``` Optional ```  | Phone number of user. |



#### Example Usage

```python
collect = {}

name = 'Name'
collect['name'] = name

address = 'Address'
collect['address'] = address

country = 'Country'
collect['country'] = country

state = 'State'
collect['state'] = state

city = 'City'
collect['city'] = city

zip = 'Zip'
collect['zip'] = zip

description = 'Description'
collect['description'] = description

email = 'email'
collect['email'] = email

phone = 'Phone'
collect['phone'] = phone


result = address_controller.address_createaddress(collect)

```


### <a name="address_listaddress"></a>![Method: ](https://apidocs.io/img/method.png ".AddressController.address_listaddress") address_listaddress

> List All Address 

```python
def address_listaddress(self,
                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | How many results to return, default is 10, max is 100, must be an integer |
| addressid |  ``` Optional ```  | addresses Sid |
| dateCreated |  ``` Optional ```  | date created address. |



#### Example Usage

```python
collect = {}

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize

addressid = 'addressid'
collect['addressid'] = addressid

date_created = 'dateCreated'
collect['date_created'] = date_created


result = address_controller.address_listaddress(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="recording_controller"></a>![Class: ](https://apidocs.io/img/class.png ".RecordingController") RecordingController

### Get controller instance

An instance of the ``` RecordingController ``` class can be accessed from the API Client.

```python
 recording_controller = client.recording
```

### <a name="create_recording_deleterecording"></a>![Method: ](https://apidocs.io/img/method.png ".RecordingController.create_recording_deleterecording") create_recording_deleterecording

> Remove a recording from your Ytel account.

```python
def create_recording_deleterecording(self,
                                         recordingsid)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recordingsid |  ``` Required ```  | The unique identifier for a recording. |



#### Example Usage

```python
recordingsid = 'recordingsid'

result = recording_controller.create_recording_deleterecording(recordingsid)

```


### <a name="create_recording_viewrecording"></a>![Method: ](https://apidocs.io/img/method.png ".RecordingController.create_recording_viewrecording") create_recording_viewrecording

> Retrieve the recording of a call by its RecordingSid. This resource will return information regarding the call such as start time, end time, duration, and so forth.

```python
def create_recording_viewrecording(self,
                                       recordingsid)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recordingsid |  ``` Required ```  | The unique identifier for the recording. |



#### Example Usage

```python
recordingsid = 'recordingsid'

result = recording_controller.create_recording_viewrecording(recordingsid)

```


### <a name="create_recording_listrecording"></a>![Method: ](https://apidocs.io/img/method.png ".RecordingController.create_recording_listrecording") create_recording_listrecording

> Retrieve a list of recording objects.

```python
def create_recording_listrecording(self,
                                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | The count of objects to return per page. |
| datecreated |  ``` Optional ```  | Filter results by creation date |
| callsid |  ``` Optional ```  | The unique identifier for a call. |



#### Example Usage

```python
collect = {}

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize

datecreated = 'Datecreated'
collect['datecreated'] = datecreated

callsid = 'callsid'
collect['callsid'] = callsid


result = recording_controller.create_recording_listrecording(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="transcription_controller"></a>![Class: ](https://apidocs.io/img/class.png ".TranscriptionController") TranscriptionController

### Get controller instance

An instance of the ``` TranscriptionController ``` class can be accessed from the API Client.

```python
 transcription_controller = client.transcription
```

### <a name="create_transcriptions_audiourltranscription"></a>![Method: ](https://apidocs.io/img/method.png ".TranscriptionController.create_transcriptions_audiourltranscription") create_transcriptions_audiourltranscription

> Transcribe an audio recording from a file.

```python
def create_transcriptions_audiourltranscription(self,
                                                    audiourl)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| audiourl |  ``` Required ```  | URL pointing to the location of the audio file that is to be transcribed. |



#### Example Usage

```python
audiourl = 'audiourl'

result = transcription_controller.create_transcriptions_audiourltranscription(audiourl)

```


### <a name="create_transcriptions_recordingtranscription"></a>![Method: ](https://apidocs.io/img/method.png ".TranscriptionController.create_transcriptions_recordingtranscription") create_transcriptions_recordingtranscription

> Transcribe a recording by its RecordingSid.

```python
def create_transcriptions_recordingtranscription(self,
                                                     recording_sid)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recordingSid |  ``` Required ```  | The unique identifier for a recording object. |



#### Example Usage

```python
recording_sid = 'recordingSid'

result = transcription_controller.create_transcriptions_recordingtranscription(recording_sid)

```


### <a name="create_transcriptions_viewtranscription"></a>![Method: ](https://apidocs.io/img/method.png ".TranscriptionController.create_transcriptions_viewtranscription") create_transcriptions_viewtranscription

> Retrieve information about a transaction by its TranscriptionSid.

```python
def create_transcriptions_viewtranscription(self,
                                                transcriptionsid)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| transcriptionsid |  ``` Required ```  | The unique identifier for a transcription object. |



#### Example Usage

```python
transcriptionsid = 'transcriptionsid'

result = transcription_controller.create_transcriptions_viewtranscription(transcriptionsid)

```


### <a name="create_transcriptions_listtranscription"></a>![Method: ](https://apidocs.io/img/method.png ".TranscriptionController.create_transcriptions_listtranscription") create_transcriptions_listtranscription

> Retrieve a list of transcription objects for your Ytel account.

```python
def create_transcriptions_listtranscription(self,
                                                options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | The count of objects to return per page. |
| status |  ``` Optional ```  | The state of the transcription. |
| dateTranscribed |  ``` Optional ```  | The date the transcription took place. |



#### Example Usage

```python
collect = {}

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize

status = StatusEnum.INPROGRESS
collect['status'] = status

date_transcribed = 'dateTranscribed'
collect['date_transcribed'] = date_transcribed


result = transcription_controller.create_transcriptions_listtranscription(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="usage_controller"></a>![Class: ](https://apidocs.io/img/class.png ".UsageController") UsageController

### Get controller instance

An instance of the ``` UsageController ``` class can be accessed from the API Client.

```python
 usage_controller = client.usage
```

### <a name="create_usage_listusage"></a>![Method: ](https://apidocs.io/img/method.png ".UsageController.create_usage_listusage") create_usage_listusage

> Retrieve usage metrics regarding your Ytel account. The results includes inbound/outbound voice calls and inbound/outbound SMS messages as well as carrier lookup requests.

```python
def create_usage_listusage(self,
                               options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| productCode |  ``` Optional ```  ``` DefaultValue ```  | Filter usage results by product type. |
| startDate |  ``` Optional ```  ``` DefaultValue ```  | Filter usage objects by start date. |
| endDate |  ``` Optional ```  ``` DefaultValue ```  | Filter usage objects by end date. |
| includeSubAccounts |  ``` Optional ```  | Will include all subaccount usage data |



#### Example Usage

```python
collect = {}

product_code = ProductCode27Enum.ALL
collect['product_code'] = product_code

start_date = '2016-09-06'
collect['start_date'] = start_date

end_date = '2016-09-06'
collect['end_date'] = end_date

include_sub_accounts = 'IncludeSubAccounts'
collect['include_sub_accounts'] = include_sub_accounts


result = usage_controller.create_usage_listusage(collect)

```


[Back to List of Controllers](#list_of_controllers)



