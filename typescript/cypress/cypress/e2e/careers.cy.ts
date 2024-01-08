import { BASE_URL } from "../support/const";
import { env } from "../support/utils";

// TODO: Convert all selectors to variables.

describe("careers", () => {
  specify("careers button", () => {
    cy.visit(BASE_URL);
    cy.xpath(env("selector_home_careers_page_href")).click();
    cy.url().should("eq", env("careers_url"));
  });

  specify("open positions button", () => {
    cy.visit(BASE_URL);
    cy.xpath(env("selector_home_careers_page_href")).click();
    cy.xpath(env("selector_careers_section_positions")).click();
    cy.url().should("eq", env("careers_url"));
  });

  specify("careers job positions", () => {
    cy.visit(env("careers_url"));
    cy.get(".tm-wrapper").each((rawElement) => {
      const title = cy.wrap(rawElement).find(".tm-title");

      // expand the job position
      title.click();

      cy.wrap(rawElement)
        .find(env("selector_careers_position_description"))
        .should("have.attr", "href")
        .and("match", /\.pdf$/);

      cy.wrap(rawElement)
        .find(env("selector_careers_position_apply_button"))
        .should("have.attr", "href")
        .and("match", /\/contact$/);
    });
  });

  specify("careers sections", () => {
    const sectionSelectors = [
      env("selector_careers_section_features"),
      env("selector_careers_section_utility"),
      env("selector_careers_section_above"),
      env("selector_careers_section_positions"),
      env("selector_careers_section_newsletter"),
    ];

    cy.visit(env("careers_url"));

    sectionSelectors.forEach((selector) => {
      cy.xpath(selector).children().should("have.length.greaterThan", 0);
    });
  });

  specify("careers filters", () => {
    cy.visit(env("careers_url"));
    const filters = cy.get(env("selector_careers_filters"));

    filters.should("have.length.greaterThan", 0);

    filters.each((rawElement) => {
      const filter = cy.wrap(rawElement);
      filter.click();

      filter.invoke("attr", "data-tag").then((dataTag) => {
        const { jobPositionsSelector, isAllFilter } =
          getJobPositionsSelector(dataTag);

        const jobPositions = cy.get(jobPositionsSelector);
        jobPositions.should("have.length.greaterThan", 0);

        if (!isAllFilter) {
          jobPositions.each((rawElement) => {
            const jobPosition = cy.wrap(rawElement);

            jobPosition
              .invoke("attr", "data-tag")
              .should("include", dataTag.split("'")[1]);
          });
        }
      });
    });
  });

  specify("newsletter subscription", () => {
    cy.visit(env("careers_url"));

    const configs = [
      [env("input_valid_email"), true],
      [env("input_invalid_email"), false],
    ];

    configs.forEach(([email, isValid]) => {
      const emailInput = cy.get(env("selector_newsletter_email_field"));
      const submitButton = cy.get(env("selector_newsletter_submit_button"));

      emailInput.clear();
      emailInput.type(email);
      submitButton.click();

      if (isValid) {
        cy.get("div.form-notification.visible")
          .should("be.visible")
          .should((element) => {
            expect(element.text().toLowerCase()).to.contain("thank you");
          });
      } else {
        cy.get(env("selector_newsletter_error_message"))
          .should("be.visible")
          .should((element) => {
            expect(element.text().toLowerCase()).to.contain("invalid");
          });
      }
    });
  });
});

const getJobPositionsSelector = (dataTag: string) => {
  if (dataTag && dataTag.includes("data-tag")) {
    const tagName = dataTag.split("'")[1];
    const jobPositionsSelector = `div.tm-wrapper[data-tag~='${tagName}']`;

    return { jobPositionsSelector, isAllFilter: false };
  }

  return { jobPositionsSelector: "div.tm-wrapper", isAllFilter: true };
};
