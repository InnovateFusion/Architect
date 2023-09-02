home = {
"initial": "Hello, how are you?, we are in the process of assisting a client to determine if they can build a home within their specified budget and time constraints. We have a set of questions and the client's answers. Based on their responses, budget limitations, time constraints, and the estimated costs of materials and labor, We will utilize cost estimations for materials and labor required to construct the home, considering the data provided in our previous discussions. Considering the budget user select residential. Make sure that the client's budget assigned for the home to be built and the estimated budget can be aligned Check the response for question number 3 budget capacity. If not, the design may not be feasible. These are the questions in order by one by one \"questions\": [{\"question\": \"Are there specific future-proofing considerations you'd like to address in the design to accommodate changing needs over time?\",\"options\": [\"A. Aging in place\", \"B. Accommodating a home office\", \"C. Energy Efficiency\", \"D. Sustainable Design\"]},{\"question\": \"Are there any cultural or religious considerations that should be integrated into the design?\",\"options\": [\"A. Prayer Room\", \"B. Cultural Symbolism\", \"C. Meditation Space\", \"D. Traditional Artifacts\"]},{\"question\": \"What is the budget range you are considering for your residential project?\",\"options\": [\"A. $10,000 - $50,000\", \"B. $50,000 - $100,000\", \"C. $100,000 - $250,000\", \"D. Over $250,000\"]},{\"question\": \"How many family members will be residing in the home?\",\"options\": [\"A. 0\", \"B. 1-3\", \"C. 4 - 7\", \"D. 8+\"]},{\"question\": \"Do you have any specific security or safety requirements for your home?\",\"options\": [\"A. Security System\", \"B. Childproofing\", \"C. Both\", \"D. None\"]},{\"question\": \"Do you require any outdoor spaces like a garden, patio, or playground for children?\",\"options\": [\"A. Garden\", \"B. Patio\", \"C. Playground\", \"D. None\"]},{\"question\": \"How many vehicles do you own, and do you need a garage or parking spaces for them?\",\"options\": [\"A. No\", \"B. 1\", \"C. 2\", \"D. 3\"]},{\"question\": \"How would you prioritize budget allocation across different aspects of the project?\",\"options\": [\"A. Construction\", \"B. Interior Finish\", \"C. Landscaping\", \"D. Equal allocation\"]},{\"question\": \"Home Space:\",\"options\": [\"A. 100 square meters\", \"B. 300+ square meters\", \"C. 500+ square meters\", \"D. 1000+ square meters\"]},{\"question\": \"How would you describe your desired atmosphere or ambiance for the interior and exterior spaces?\",\"options\": [\"A. Cozy\", \"B. Minimalist\", \"C. Elegant\", \"D. Modern\"]},{\"question\": \"Are there any specific design inspirations, such as a favorite vacation destination or art movement, that you'd like to draw upon for interior design?\",\"options\": [\"A. Color Picker\", \"B. Vintage\", \"C. Contemporary\", \"D. Natural\"]},{\"question\": \"Are you open to incorporating smart home technology for automation and control of various home systems?\",\"options\": [\"A. Security\", \"B. Lighting\", \"C. Entertainment\", \"D. All of the above\"]},{\"question\": \"Are there any weather-related concerns or considerations for your project, such as extreme temperatures or heavy rainfall during certain seasons?\",\"options\": [\"A. Extreme Temperature\", \"B. Heavy Raining\", \"C. Both\", \"D. None\"]},{\"question\": \"Have you thought about construction phasing if you need to occupy parts of the home before the entire project is completed?\",\"options\": [\"A. YES\", \"B. NO\", \"C. Not sure\", \"D. Partial occupancy planned\"]}]. Don't type anything else. Don't worry, I will guide you through the process. I will not ask all the questions at once. I will ask one question at a time. Please only respond in the given format only. If you are ready to begin, please type {\"status\": \"success\"}. If you are not ready to begin, please type  {\"status\": \"fail\"}. only in json format. use double quotes for keys and values."
}

message_for_design = {
    1: "The client has provided the following responses to the questions: {answers}. ",
    2: "Based on this client response, design a home for the client's preferences, budget, and time constraints. If the response succeeds, return in this format: ",
    3: "If the response fails, return in this format:",
    4: "Please provide the design and analysis based on the client's responses. Return a response in json format only. use double quotes for keys and values."
}

succes_response = {
    "status": "success",
    "feasibility": "yes or no. if the estimated budget (client budget - response for question number 3) is less than or equal to the overall cost of the project, it is feasible (yes), otherwise, it is not feasible (no).",
    "home_appearance": {
        "interior_style": "Recommended Interior Style",
        "exterior_style": "Recommended Exterior Style",
        "color_palette": "Recommended Color Palette",
        "architectural_features": "Recommended Architectural Features",
        "numberOfclass": "X",
        "numberOffloor": "X"
    },
    "budget_analysis": {
        "estimated_budget": "$XXX,XXX",
        "budget_allocation": ["Recommended Budget Allocation"],
        "suggested_changes": "Detailed information on suggested changes to align with the budget. This includes any cost-cutting measures or alternative materials.",
        "detailed_material_costs": ["steel_bar: $XX,XXX", "concrete: $XX,XXX", "wood: $XX,XXX", "others"],
        "labor_costs": "$XX,XXX"
    },
    "timeline_analysis": {
        "estimated_timeline": "XX months",
        "phasing_details": {
            "description": "The project can be divided into XX phases for XX occupations.",
            "phases": ["detail info phase X", "detail info phase X"]
        }
    },
    "recommendations": [
        "Additional recommendations for enhancing the project based on the client's needs and preferences.",
        "These could include specific design elements, technology integrations, or sustainability features."
    ]
}

fail_response = {
    "status": "error"
}

answers = {
        "future_proofing": ["A. Aging in place", "B. Accommodating a home office"],
        "cultural_religious": ["A. Prayer Room", "B. Cultural Symbolism"],
        "budget_range": "A. $10,000 - $50,000",
        "family_size": "C. 4 - 7",
        "security_safety": "C. Both",
        "outdoor_spaces": ["A. Garden", "B. Patio"],
        "vehicles_parking": "C. 2",
        "budget_allocation": "D. Equal allocation",
        "home_space": "B. 300+ square meters",
        "atmosphere_ambiance": "C. Elegant",
        "design_inspirations": "D. Natural",
        "smart_home_technology": "D. All of the above",
        "weather_concerns": "A. Extreme Temperature",
        "construction_phasing": "A. YES"
    }

examples = {
  "status": "success",
  "feasibility": "yes",
  "home_appearance": {
    "interior_style": "Elegant",
    "exterior_style": "Modern",
    "color_palette": "Natural Tones",
    "architectural_features": "Open floor plan, large windows",
    "numberOfclass": "4",
    "numberOffloor": "2"
  },
  "budget_analysis": {
    "estimated_budget": "$85,000",
    "budget_allocation": [
      "Construction: $28,333",
      "Interior Finish: $28,333",
      "Landscaping: $28,334"
    ],
    "suggested_changes": "Consider using more cost-effective materials for interior finishes and landscaping.",
    "detailed_material_costs": [
      "concrete: $15,000",
      "wood: $20,000",
      "paint: $5,000",
      "others"
    ],
    "labor_costs": "$16,000"
  },
  "timeline_analysis": {
    "estimated_timeline": "12 months",
    "phasing_details": {
      "description": "The project can be divided into 3 phases for occupation.",
      "phases": [
        "Phase 1: Foundation and framing",
        "Phase 2: Interior finishing and landscaping",
        "Phase 3: Final touches and move-in"
      ]
    }
  },
  "recommendations": [
    "Consider integrating smart home technology for automation and control of various home systems.",
    "Explore energy-efficient options and sustainable design practices."
  ]
}

business = {
  "initial": "\"Hello, we are assisting a client in determining if they can build a business building within budget and time constraints, using a set of questions and client answers, aligned with budget and feasibility checks, and presenting questions one by one.\", \"questions\": [{\"question\": \"What is the primary purpose or function of the business building?\", \"options\": [\"A. Office Space\", \"B. Retail Space\", \"C. Manufacturing\", \"D. Mixed-Use\"]}, {\"question\": \"What is the estimated total square footage required for the building?\", \"options\": [\"A. Under 10,000 sq ft\", \"B. 10,000 - 50,000 sq ft\", \"C. 50,000 - 100,000 sq ft\", \"D. Over 100,000 sq ft\"]}, {\"question\": \"Do you have any specific architectural style preferences for the building?\", \"options\": [\"A. Modern\", \"B. Traditional\", \"C. Contemporary\", \"D. Industrial\"]}, {\"question\": \"Are there any sustainability or environmental goals for the project?\", \"options\": [\"A. LEED Certification\", \"B. Energy Efficiency\", \"C. Green Roof\", \"D. None\"]}, {\"question\": \"How many floors or levels should the building have?\", \"options\": [\"A. Single-Story\", \"B. 2-3 Floors\", \"C. 4-6 Floors\", \"D. More than 6 Floors\"]}, {\"question\": \"Are there any zoning or regulatory constraints to consider?\", \"options\": [\"A. Yes\", \"B. No\", \"C. Not sure\", \"D. Local authorities' approval required\"]}, {\"question\": \"How many employees or occupants will the building house?\", \"options\": [\"A. Under 50\", \"B. 50-200\", \"C. 200-500\", \"D. Over 500\"]}, {\"question\": \"Are there any specialized spaces required, such as laboratories or conference rooms?\", \"options\": [\"A. Yes, specialized spaces\", \"B. Standard office spaces\", \"C. Mix of specialized and standard spaces\", \"D. Not sure\"]}, {\"question\": \"Do you have specific accessibility requirements, such as ramps or elevators?\", \"options\": [\"A. Yes, accessibility\", \"B. Basic accessibility features\", \"C. Limited accessibility requirements\", \"D. Not sure\"]}, {\"question\": \"Are there any desired amenities or common spaces, like a cafeteria or fitness center?\", \"options\": [\"A. Yes, extensive amenities\", \"B. Basic amenities\", \"C. Limited amenities\", \"D. Not sure\"]}, {\"question\": \"How many parking spaces do you anticipate needing for employees and visitors?\", \"options\": [\"A. No parking required\", \"B. Limited parking spaces\", \"C. Sufficient parking for employees and visitors\", \"D. Public transportation access\"]}, {\"question\": \"What atmosphere or ambiance do you desire for the interior and exterior spaces?\", \"options\": [\"A. Modern and Innovative\", \"B. Professional and Classic\", \"C. Contemporary and Open\", \"D. Other (please specify)\"]}, {\"question\": \"Are there any specific design inspirations or branding elements to incorporate into the interior design?\", \"options\": [\"A. Brand Colors and Logo\", \"B. Industry Themes\", \"C. Artistic Statements\", \"D. Neutral/None\"]}, {\"question\": \"Are you open to incorporating advanced technology for building automation, security, and energy efficiency?\", \"options\": [\"A. Smart Building Systems\", \"B. Security and Access Control\", \"C. Energy Management\", \"D. All of the above\"]}, {\"question\": \"Are there any weather-related concerns or site-specific challenges for your project?\", \"options\": [\"A. Extreme Weather\", \"B. Site Challenges\", \"C. Both\", \"D. None\"]}]}  Don't type anything else. Don't worry, I will guide you through the process. I will not ask all the questions at once. I will ask one question at a time. Please only respond in the given format only. If you are ready to begin, please type {\"status\": \"success\"}. If you are not ready to begin, please type  {\"status\": \"fail\"}. only in json format. use double quotes for keys and values."
  }


business_answer_sample = {
    "status": "success",
    "feasibility": "yes or no. If the estimated budget (client budget - response for question number 3) is less than or equal to the overall cost of the project, it is feasible (yes), otherwise, it is not feasible (no).",
    "building_details": {
        "building_purpose": "Recommended Building Purpose",
        "total_square_footage": "Recommended Total Square Footage",
        "architectural_style": "Recommended Architectural Style",
        "sustainability_goals": ["Recommended Sustainability Goals"],
        "number_of_floors": "Recommended Number of Floors",
        "zoning_constraints": "Recommended Zoning Constraints"
    },
    "occupancy_details": {
        "number_of_occupants": "Recommended Number of Occupants",
        "specialized_spaces_required": "Recommended Specialized Spaces",
        "accessibility_requirements": "Recommended Accessibility Requirements",
        "amenities": "Recommended Amenities",
        "parking_spaces": "Recommended Parking Spaces"
    },
    "design_preferences": {
        "interior_exterior_ambiance": "Recommended Interior and Exterior Ambiance",
        "design_inspirations": ["Recommended Design Inspirations"],
        "technology_integration": "Recommended Technology Integration"
    },
    "construction_and_timing": {
        "weather_site_challenges": "Recommended Weather and Site Challenges",
        "construction_phasing": "Recommended Construction Phasing"
    },
    "budget_analysis": {
        "estimated_budget": "Recommended Estimated Budget",
        "budget_allocation": ["Recommended Budget Allocation"],
        "suggested_changes": "Detailed information on suggested changes to align with the budget. This includes any cost-cutting measures or alternative materials.",
        "detailed_material_costs": ["Recommended Material Costs"],
        "labor_costs": "Recommended Labor Costs"
    },
    "timeline_analysis": {
        "estimated_timeline": "Recommended Estimated Timeline",
        "phasing_details": {
            "description": "The project can be divided into recommended phases for efficient construction.",
            "phases": ["Recommended Phase Details"]
        }
    },
    "recommendations": [
        "Additional recommendations for enhancing the project based on the client's needs and preferences.",
        "These could include specific design elements, technology integrations, or sustainability features."
    ]
}

business_answer_example = {
  "status": "success",
  "feasibility": "yes",
  "building_details": {
    "building_purpose": "Office Space",
    "total_square_footage": "50,000 - 100,000 sq ft",
    "architectural_style": "Modern",
    "sustainability_goals": ["Energy Efficiency", "Green Roof"],
    "number_of_floors": "4-6 Floors",
    "zoning_constraints": "Local authorities' approval required"
  },
  "occupancy_details": {
    "number_of_occupants": "200-500",
    "specialized_spaces_required": "Mix of specialized and standard spaces",
    "accessibility_requirements": "Basic accessibility features",
    "amenities": "Basic amenities",
    "parking_spaces": "Sufficient parking for employees and visitors"
  },
  "design_preferences": {
    "interior_exterior_ambiance": "Contemporary and Open",
    "design_inspirations": ["Brand Colors and Logo", "Industry Themes"],
    "technology_integration": "All of the above"
  },
  "construction_and_timing": {
    "weather_site_challenges": "Both",
    "construction_phasing": "Partial occupancy planned"
  },
  "budget_analysis": {
    "estimated_budget": "$5,000,000",
    "budget_allocation": [
      "Construction: $2,000,000",
      "Interior Finish: $1,500,000",
      "Landscaping: $500,000",
      "Technology Integration: $500,000",
      "Others: $1,000,000"
    ],
    "suggested_changes": "Explore cost-effective construction methods and materials."
  },
  "timeline_analysis": {
    "estimated_timeline": "24 months",
    "phasing_details": {
      "description": "The project can be divided into 4 phases for efficient construction.",
      "phases": [
        "Phase 1: Site Preparation and Foundation",
        "Phase 2: Structural Construction",
        "Phase 3: Interior Finishing",
        "Phase 4: Technology Integration and Move-In"
      ]
    }
  },
  "recommendations": [
    "Consider using sustainable materials to align with sustainability goals.",
    "Engage with local authorities early to streamline zoning approvals.",
    "Incorporate energy-efficient HVAC and lighting systems for long-term cost savings."
  ]
}
