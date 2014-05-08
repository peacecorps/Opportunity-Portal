Opportunity Portal README
========================

<h1>Peace Corps Job Listing Project</h1>

<h2>Business Opportunity:</h2>  

Posting detailed job listings related to a new shorter, faster application process are key steps in becoming even more transparent and modernized as an Agency.  This project will make it possible for prospective Volunteers to view descriptive information about a specific Volunteer job on peacecorps.gov and our mobile site.  For the short-term (July 1st), a job listing will include an “apply” prompt to start an application (to the Peace Corps generally) but the applicant will have the ability to inform Peace Corps recruitment of their interest in the specific assignment that was posted.  Eventually, the prospect will be able to apply directly (and seamlessly) to that specific position. 

<h2>Assignment:</h2>  

Create a user-friendly display with sort/filtering functionality of Peace Corps Volunteer job listings that allow users to sort through Volunteer openings and find more detailed information about that specific position.   Critical in this development progress, is ensuring that the prototype developed will integrate with the Peace Corps existing website and is responsive/platform agnostic. 

<h2>Background Information:</h2>

•	Peace Corps website is built on: Python / Django.
•	Job listing data will be populated with a FTP data transfer parsed out to a webpage.
•	Job listing fields are listed below for July 1st and with “hidden” fields indicated that will not be used initially but may be activated and included in the job listings in a Phase 2 (note:  we may want to think about making some of these fields sortable, e.g., language).

<h2>Timeline and Tasks:</h2>

<h3>Tasks by June 1:</h3>

FIRST STEPS
•	Introductory Google Hangout call on Monday May 5th 
•	Determine rolls for developers able to help out and commit to timeline
•	Identify additional talent needs and individuals requiring outreach, any crowd sourcing requirements
•	Determine regular meeting schedule with conference call line between Devs and Peace Corps
•	Dev Team determine GitHub Set up in Peace Corps repository. https://github.com/PeaceCorps
•	What additional collaborative spaces are required to set up? UI Design sites for collaboration...?

STAGING SITE
•	PC determine hosting environment for Staging site
•	Devs creating non-Peace Corps development portal to host versions of site
•	PC and Devs configuring hackathon site to function on Staging environment for iterative development Integration
•	Review options for integrating DOVE database of volunteer opportunities with Discovery Portal
•	Test agreed implementation on Staging
•	Review approach and adjust as necessary
•	Test any updated integration on Staging
•	User Testing
•	Send non-technical internal users to Staging site for user feedback
•	Collect and ticket feedback on GitHub
•	Make iterative design changes to Staging/Production

<h3>Tasks by July 1:</h3>

LAUNCH
•	Swap Staging and Production sites to make discovery portal public

<h2>Technical Requirements:</h2>

•	Responsive design
•	Filtering/sorting by:  Region, Country, Departure Date, and Sector by July 1st
•	Integration into Peace Corps Framework (ideal to leverage site established parameters for items like “Pop-up” windows, etc.)
•	Data pull/display from webpage (server to server)
•	Design works with Peace Corps brand
•	Leverage digital assets that are accurate (and we have permission)
•	OUTSTANDING – how to incorporate medical information (TBD for discussion)
•	OUTSTANDING – how to incorporate the “know by” date (TBD for discussion)

<h2>Information to Display</h2>

<h3>The following is a list of fields that will be displayed in some fashion to potential applicants:</h3>

Volunteers Requested
  Label to Use: "Volunteers Requested"
  Sort/Filter: No
  Notes: Indicates # of positions available. (Number that is unlikely to fluctuate once posted)

Sub-Region
  Label to Use: "Region"
  Sort/Filter: Yes
  Notes: none
  
Post
  Label to Use: "Country"
  Sort/Filter: Yes
  Notes: none
  
Staging Start Date
  Label to Use: "Departure Date"
  Sort/Filter: Yes
  Notes: none
  
Project Title
  Label to Use: "Project Title"
  Sort/Filter: No
  Notes: Note:  We will strip out the Code (first 7 characters in field) and make this into a new listing
  
Sector
  Label to Use: "Sector"
  Sort/Filter: Yes
  Notes: none
  
Desired Skills
  Label to Use: "Desired Skills"
  Sort/Filter: No
  Notes: none
  
Project Desciption
  Label to use: "Project Description"
  Sort/Filter: No
  Notes: none

<h3>The following fields will not be displayed on the initial launch, but will be incorporated in a future release.</h3>
  
Living Conditions
  Label to Use: "Living Conditions"
  Sort/Filter: No
  Notes: Text Field
  
Language Requirements
  Label to Use: "Language"
  Sort/Filter: Yes
  Notes: Text Field
  
Accepts Couples
  Label to Use: "Accepts Couples"
  Sort/Filter: No
  Notes: Number field, but may also include text

<h2>Resources and Reference Files:</h2>

•	Link Prezi: http://prezi.com/4tmjrjejipqh/?utm_campaign=share&utm_medium=copy
•	PCOI: http://pcoi.herokuapp.com/
•	Peace Corps Opportunity Search: http://peace-corps-search.herokuapp.com/
•	Another Prototype: http://peacecorps.meteor.com/
•	MIT hackathon submissions with screenshots: http://idhack.challengepost.com/submissions

<h2>Considerations based on Hack-a-thon prototypes: (Remove from ReadMe and Ticket)</h2>

•	Quick view:  positions open/application/notification date/departure date
•	Ability to bookmark this job/saving/social icons
•	Pop-up/window detail page (can you still bookmark?)
•	Use of sector icons
•	(HeroKuapp.com) Not sure truncated project description works as well as short description (or appeal) to lead into longer description
•	(Meteor.com) Pick-a-date slide ruler functionality interesting—need to use correctly 
•	(MIT) Guided Search and use of filtering system (box check without having to create new search each time)
•	(Ops) Like brief description of sector
•	(Corp Connect) – Like filtering capabilities



