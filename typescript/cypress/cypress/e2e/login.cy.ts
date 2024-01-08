import { BASE_URL } from "../support/const";
import { env } from "../support/utils";

describe("login", () => {
  specify("login valid", () => {
    cy.visit(BASE_URL);
    cy.xpath(env("selector_login_button")).click();
    cy.xpath(env("selector_email_field")).type(env("input_valid_email"));
    cy.xpath(env("selector_password_field")).type(env("input_valid_password"));
    cy.xpath(env("selector_password_field")).type("{enter}");

    // TODO: We can add a check for the landing URL after login
    // if we had credentials.
    // cy.url().should('include', '/dashboard');

    // TODO: We can find an element after a successful login.
  });

  specify("valid email invalid password", () => {
    cy.visit(BASE_URL);
    cy.xpath(env("selector_login_button")).click();
    cy.xpath(env("selector_email_field")).type(env("input_valid_email"));
    cy.xpath(env("selector_password_field")).type(
      env("input_invalid_password")
    );
    cy.xpath(env("selector_password_field")).type("{enter}");

    cy.xpath(env("selector_login_notification")).should("exist");
  });

  specify("invalid email valid password", () => {
    cy.visit(BASE_URL);
    cy.xpath(env("selector_login_button")).click();
    cy.xpath(env("selector_email_field")).type(env("input_invalid_email"));
    cy.xpath(env("selector_password_field")).type(env("input_valid_password"));
    cy.xpath(env("selector_password_field")).type("{enter}");

    cy.xpath(env("selector_login_notification")).should("exist");
  });

  specify("invalid email invalid password", () => {
    cy.visit(BASE_URL);
    cy.xpath(env("selector_login_button")).click();
    cy.xpath(env("selector_email_field")).type(env("input_invalid_email"));
    cy.xpath(env("selector_password_field")).type(
      env("input_invalid_password")
    );
    cy.xpath(env("selector_password_field")).type("{enter}");

    cy.xpath(env("selector_login_notification")).should("exist");
  });

  specify("unregistered email valid password", () => {
    cy.visit(BASE_URL);
    cy.xpath(env("selector_login_button")).click();
    cy.xpath(env("selector_email_field")).type(env("input_unregistered_email"));
    cy.xpath(env("selector_password_field")).type(env("input_valid_password"));
    cy.xpath(env("selector_password_field")).type("{enter}");

    cy.xpath(env("selector_login_notification")).should("exist");
  });

  specify("registered email invalid password", () => {
    cy.visit(BASE_URL);
    cy.xpath(env("selector_login_button")).click();
    cy.xpath(env("selector_email_field")).type(env("input_registered_email"));
    cy.xpath(env("selector_password_field")).type(
      env("input_invalid_password")
    );
    cy.xpath(env("selector_password_field")).type("{enter}");

    cy.xpath(env("selector_login_notification")).should("exist");
  });

  specify("valid email empty password", () => {
    cy.visit(BASE_URL);
    cy.xpath(env("selector_login_button")).click();
    cy.xpath(env("selector_email_field")).type(env("input_valid_email"));
    cy.xpath(env("selector_password_field")).type("{enter}");

    cy.xpath(env("selector_login_notification")).should("exist");
  });

  specify("empty email valid password", () => {
    cy.visit(BASE_URL);
    cy.xpath(env("selector_login_button")).click();
    cy.xpath(env("selector_password_field")).type(env("input_valid_password"));
    cy.xpath(env("selector_password_field")).type("{enter}");

    cy.xpath(env("selector_login_notification")).should("exist");
  });

  specify("empty email empty password", () => {
    cy.visit(BASE_URL);
    cy.xpath(env("selector_login_button")).click();
    cy.xpath(env("selector_password_field")).type("{enter}");

    cy.xpath(env("selector_login_notification")).should("exist");
  });

  specify("forgot password valid email", () => {
    cy.visit(BASE_URL);
    cy.xpath(env("selector_login_button")).click();
    cy.xpath(env("selector_login_forgot_password_link")).click();
    cy.xpath(env("selector_email_field_forgot_password")).type(
      env("input_valid_email")
    );
    cy.xpath(env("selector_email_field_forgot_password")).type("{enter}");

    cy.contains(env("selector_expected_text_in_password_confirmation")).should(
      "exist"
    );
  });

  specify("forgot password invalid email", () => {
    cy.visit(BASE_URL);
    cy.xpath(env("selector_login_button")).click();
    cy.xpath(env("selector_login_forgot_password_link")).click();
    cy.xpath(env("selector_email_field_forgot_password")).type(
      env("input_invalid_email")
    );
    cy.xpath(env("selector_email_field_forgot_password")).type("{enter}");

    cy.url().should("include", "/Account/ForgotPassword");
  });

  specify("forgot password without email", () => {
    cy.visit(BASE_URL);
    cy.xpath(env("selector_login_button")).click();
    cy.xpath(env("selector_login_forgot_password_link")).click();
    cy.xpath(env("selector_email_field_forgot_password")).type("{enter}");

    cy.url().should("include", "/Account/ForgotPassword");
  });
});
