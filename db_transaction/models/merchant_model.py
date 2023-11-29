from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, DateTime, Boolean, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from db_transaction.models.role_model import Role

Base = declarative_base()


class Merchant(Base):
    __tablename__ = 'Merchant'
    _id = Column(String, primary_key=True)

    commercial_registration_number = Column(String)
    commercial_title = Column(String)
    communication_contact_building_number = Column(String)
    communication_contact_county_selection = Column(String)
    communication_contact_descriptive_address = Column(String)
    communication_contact_district = Column(String)
    communication_contact_email1 = Column(String)
    communication_contact_first_name = Column(String)
    communication_contact_landline_phone_number = Column(String)
    communication_contact_last_name = Column(String)
    communication_contact_mobile_phone_number = Column(String)
    communication_contact_national_identity_number = Column(String)
    communication_contact_postal_code = Column(String)
    communication_contact_province_code = Column(String)
    communication_contact_province_selection = Column(String)
    communication_contact_street = Column(String)
    company_alias_name = Column(String)
    company_name = Column(String)
    csrf_token = Column(String)
    customer_service_e_mail_address = Column(String)
    definition_status = Column(String)
    epdk_licence_number = Column(String)
    finance_contact_building_number = Column(String)
    finance_contact_county_selection = Column(String)
    finance_contact_descriptive_address = Column(String)
    finance_contact_district = Column(String)
    finance_contact_email1 = Column(String)
    finance_contact_first_name = Column(String)
    finance_contact_landline_phone_number = Column(String)
    finance_contact_last_name = Column(String)
    finance_contact_mobile_phone_number = Column(String)
    finance_contact_national_identity_number = Column(String)
    finance_contact_postal_code = Column(String)
    finance_contact_province_code = Column(String)
    finance_contact_province_selection = Column(String)
    finance_contact_street = Column(String)
    is_active = Column(Boolean)
    lpg_epdk_licence_number = Column(String)
    merchant_number = Column(Integer)
    merchant_office_code = Column(String)
    merchant_office_name = Column(String)
    merchant_office_number = Column(String)
    mersis_number = Column(String)
    national_id = Column(String)
    shipping_contact_building_number = Column(String)
    shipping_contact_county_selection = Column(String)
    shipping_contact_descriptive_address = Column(String)
    shipping_contact_district = Column(String)
    shipping_contact_email1 = Column(String)
    shipping_contact_first_name = Column(String)
    shipping_contact_landline_phone_number = Column(String)
    shipping_contact_last_name = Column(String)
    shipping_contact_mobile_phone_number = Column(String)
    shipping_contact_national_identity_number = Column(String)
    shipping_contact_postal_code = Column(String)
    shipping_contact_province_code = Column(String)
    shipping_contact_province_selection = Column(String)
    shipping_contact_street = Column(String)
    tax_identification_number = Column(String)
    tax_number = Column(String)
    technical_contact_building_number = Column(String)
    technical_contact_county_selection = Column(String)
    technical_contact_descriptive_address = Column(String)
    technical_contact_district = Column(String)
    technical_contact_email1 = Column(String)
    technical_contact_first_name = Column(String)
    technical_contact_landline_phone_number = Column(String)
    technical_contact_last_name = Column(String)
    technical_contact_mobile_phone_number = Column(String)
    technical_contact_national_identity_number = Column(String)
    technical_contact_postal_code = Column(String)
    technical_contact_province_code = Column(String)
    technical_contact_province_selection = Column(String)
    technical_contact_street = Column(String)
    trade_name = Column(String)
    user_from = Column(String)
    web_address = Column(String)

    created_date = Column(DateTime)
    # Diğer sütunlar buraya eklenir
    role_id = Column(ForeignKey(Role.id))
    admins = relationship(Role, backref="Admins")
