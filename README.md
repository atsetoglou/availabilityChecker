<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

# Availability Checker

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#preparation-to-use">Preparation To Use</a></li>
      </ul>
    </li>
    <li><a href="#usage-example">Usage Example</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About The Project

This is a Python script that will check the availability of a product on a website every hour and will inform the user by mail when the wanted article will be in stock.

<p align="right">(<a href="#top">back to top</a>)</p>

## Getting Started

### Prerequisites
* selenium
    ```sh
    pip install selenium
    ```
* An email address that will allow access to less secure apps [(gmail example)](https://support.google.com/accounts/answer/6010255?authuser=6&p=lsa_blocked&hl=en&authuser=6&visit_id=637776810165160052-4083104164&rd=1#zippy=%2Cif-less-secure-app-access-is-on-for-your-account).

### Preparation To Use

1. Clone the repository
    ```sh
    git clone git@github.com:atsetoglou/availabilityChecker.git
    ```
2. Modify the file `main.py`\
    In fact, in this part you will need to adapt the script to your needs. More specifically:
    * In the function `sendEmail(link)` you will have to change the variables: `email`, `password`, `mailTo` and `subject` (optional).
    * You will also need to change the variables: 
        * `links`: A list containing all the urls you want to visit.
        * `isAvailable`: The motif that will verify if a product is available.
        * `availability`: See Usage Example.
        * `cookies_button`: See Usage Example.

<p align="right">(<a href="#top">back to top</a>)</p>

## Usage Example
For this example we are going to check the availability of a product on https://www.amazon.fr/.
Having already set the variables that concern the function `sendEmail(link)` we are going to set the rest of variables.
* `links`:
    ```python
    links = ["https://www.amazon.fr/dp/B08C1KN5J2/ref=cm_sw_em_r_mt_dp_dl_D4MHDX62RZ72ZYB226PJ"]
    ```

* `isAvailable`: All we have to do is visit the page of a product that is available and see what appears in the section. In the case of the example, the motif is "En stock.".
    ```python
    isAvailable = "En stock."
    ```
    ![isAvailable](https://github.com/atsetoglou/availabilityChecker/blob/main/resources/images/isAvailable.png?raw=true)

    If we want to avoid any mistakes, it will be safer to find the motif throught the inspection of our web browser.\
    ![isAvailable_source](https://github.com/atsetoglou/availabilityChecker/blob/main/resources/images/isAvailable_source.png?raw=true)

* `availability`: For this variable, we are going to need the `id` or the `class` where the availability of the product appears on the source of the page. In our case we are going to use the `id` which is `availability`.
    ```python
    availability = browser.find_element(By.ID, "availability")
    ```
    ![id_availability](https://github.com/atsetoglou/availabilityChecker/blob/main/resources/images/id_availability.png?raw=true)

* `cookies_button`: Similarly to `availability`, we are going to need the `id` or the `class` of the `Accept Cookies` button. In our case we are going to use the `id` which is `sp-cc-accept`.
    ```python
    cookies_button = browser.find_element(By.ID, "sp-cc-accept")
    ```
    ![id_cookies_button](https://github.com/atsetoglou/availabilityChecker/blob/main/resources/images/id_cookies_button.png?raw=true)

Once we have changed all the variables we can now run the script. If the product we are searching is available we will receive a mail like the following one:

![mail_example](https://github.com/atsetoglou/availabilityChecker/blob/main/resources/images/mail_example.png?raw=true)

<p align="right">(<a href="#top">back to top</a>)</p>

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add some NewFeature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

## Contact

Apostolos Tsetoglou - [Linkedin](https://www.linkedin.com/in/apostolos-tsetoglou/)\
Email: tsetoglou.a@gmail.com

Project Link: [https://github.com/atsetoglou/availabilityChecker](https://github.com/atsetoglou/availabilityChecker)

<p align="right">(<a href="#top">back to top</a>)</p>


[contributors-shield]: https://img.shields.io/github/contributors/atsetoglou/availabilityChecker?style=for-the-badge
[contributors-url]: https://github.com/atsetoglou/availabilityChecker/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/atsetoglou/availabilityChecker?style=for-the-badge
[forks-url]: https://github.com/atsetoglou/availabilityChecker/network/members
[stars-shield]: https://img.shields.io/github/stars/atsetoglou/availabilityChecker?style=for-the-badge
[stars-url]: https://github.com/atsetoglou/availabilityChecker/stargazers
[issues-shield]: https://img.shields.io/github/issues/atsetoglou/availabilityChecker?style=for-the-badge
[issues-url]: https://github.com/atsetoglou/availabilityChecker/issues
[license-shield]: https://img.shields.io/github/license/atsetoglou/availabilityChecker?style=for-the-badge
[license-url]: https://github.com/atsetoglou/availabilityChecker/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/apostolos-tsetoglou/